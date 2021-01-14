#!/usr/bin/env python3
import argparse
import fileinput
import logging
import os
import re
from statistics import mean, median, stdev
import sys
import time
import threading


class VideoStartTimeRecord:
    """Holds each individual record parsed."""

    def __init__(self, groupdict):
        for k, v in groupdict.items():
            setattr(self, k, v)

    def __str__(self):
        return '\n'.join(
            [str(i) + '=' + getattr(self, i) for i in vars(self)])


class RemoteCommand:
    """Controls the TV by executing remote commands.

    Disables async kernel logging that messes with Roku OS logging as it's not
    synchronized. Disables most Roku OS logging letting only on what we're
    actually interested in. Sets default media player parameters.
    """

    _23_cmd_template = ('{1} | nc -t -w 3 {0} 23 >/dev/null 2>&1')

    _8060_cmd_template = ('curl -s -S -i -X POST http://{0}:8060/{1} '
                          '2>&1 | grep -vE "HTTP\\/1\\.1 200|Server|Content"')

    _8080_cmd_template = ('{1} | nc {0} 8080 2>&1 | grep -vE "Roku TV|>>"')

    def __init__(self, ip):
        self.ip = ip
        self.channel_name = 'Unknown'
        self._setup_remote_environment()

    def _setup_remote_environment(self):
        print('Setting up the remote environment...')
        assert(os.system(self._23_cmd_template.format(
            self.ip, ('{ echo -e "dmesg -n 1\n"; usleep 1500000; '
                      'echo -e "\x1dclose\x0d"; }'))) == 0)
        debug_cmds = '\n'.join([
            'log -c *',
            'log +S',
            'log +c km.mp.play.start.det',
            'config_set fw.mp.dash.distance-from-live 24',
            'config_set fw.mp.dash.enable-gap-compensator.live 0',
            'config_set fw.mp.dash.enable-gap-compensator.vod 0',
            'config_set fw.mp.dash.enable-reseek-on-gap.live 0',
            'config_set fw.mp.dash.enable-reseek-on-gap.vod 0',
        ])
        assert(os.system(self._8080_cmd_template.format(
            self.ip, 'echo -e "{}"'.format(debug_cmds))) <= 256)

    def _send_keypress(self, key):
        os.system(self._8060_cmd_template.format(self.ip, 'keypress/' + key))

    def change_channel(self):
        print('Changing channel...')


class PressBackSelect(RemoteCommand):
    """Defines a policy for changing channels based on pressing Back (to exit
    a video playing app) followed by pressing Select (to launch the app again).
    """

    def __init__(self, ip):
        super().__init__(ip)
        self.channel_name = 'BigBuckBunny Sample'

    def change_channel(self):
        super().change_channel()
        self._send_keypress('Back')
        time.sleep(2)
        self._send_keypress('Select')
        time.sleep(1)


class PressLeft(RemoteCommand):
    """Defines a policy for changing channels based solely on pressing Left."""

    def __init__(self, ip):
        super().__init__(ip)
        self.channel_name = 'DirecTV'

    def change_channel(self):
        super().change_channel()
        self._send_keypress('Left')
        time.sleep(1)


class VideoStartTimeParser:
    """Scans input (a file or a serial port device) continuously and tries to
    match it against the video start time key metric, driving the TV if needed.

    Parses km.mp.play.start.det log messages and extracts its fields into a
    parsed record, which is then accumulated for later analysis. Once a log
    record is parsed successfully, it immediately requests TV to play another
    video, making it possible to gather the video start time measurements as
    fast as possible.
    """

    _re = r'''
              ^                                             # line anchor
              (?P<timestamp>[\d\-]*\ [\d\:\.]*)             # timestamp
              \ *\*?\[(?P<logid>.*)\]                       # logid
              \ sess=(?P<sess>\w*)                          # sess
              \ contid=(?P<contid>.*)                       # contid
              \ chanid=(?P<chanid>\w*)                      # chanid
              \ ctype=(?P<ctype>\w*)                        # ctype
              \ eventtype=(?P<eventtype>\w*)                # eventtype
              \ cpu=(?P<cpu>\d*)                            # cpu
              \ play=(?P<play>\d*)                          # play
              \ unpause=(?P<unpause>\d*)                    # unpause
              \ render=(?P<render>\d*)                      # render
              \ dmxctor=(?P<dmxctor>\d*)                    # dmxctor
              \ manparse=(?P<manparse>[\d\-]*)              # manparse
              \ drmload=(?P<drmload>[\d\-]*)                # drmload
              \ licacq=(?P<licacq>[\d\-]*)                  # licacq
              \ preroll=(?P<preroll>[\d\-]*)                # preroll
              \ drm-sys=(?P<drmsys>.*)                      # drm-sys
              \ mansize=(?P<mansize>[\d\-]*)                # mansize
              \ parsecnt=(?P<parsecnt>[\d\-]*)              # parsecnt
              \ periodcnt=(?P<periodcnt>[\d\-]*)            # periodcnt
              \ a\/vrepcnt=(?P<avrepcnt>[\d\-\/]*)          # a/vrepcnt
              \ dmxctor=(?P<dmxctor1>[\d\-]*)               # dmxctor
              \ decpreroll=(?P<decpreroll>[\d\-]*)          # decpreroll
              \ prebuffer=(?P<prebuffer>[\d\-]*)            # prebuffer
              \ prebuffer-required=(?P<prebufferrec>[\d]*)  # prebuffer-required
              \ prebuffer-actual=(?P<prebufferact>[\d-]*)   # prebuffer-actual
              \ licacq-more=(?P<licacqmore>[\d\-]*)         # licacq-more
              \ stream-fmt-detect=(?P<streamfmtdet>[\d\-]*) # stream-fmt-detect
              .*                                            # suffix
           '''

    class ChannelChangerThread(threading.Thread):
        """Listens for a notification from the parser and as soon as a record
        has been parsed successfully, it controls the TV to start another video
        playback immediately. If no logs are parsed within a specified timeout,
        it drives TV to try playing another video anyway.
        """

        def __init__(self, cv, cmd_change_channel):
            threading.Thread.__init__(self, name=self.__class__.__name__)
            self.cv = cv
            self._cmd_change_channel = cmd_change_channel
            self.should_stop = False
            self.do_channel_change_now = False
            self.CHANGE_CHANNEL_RETRY_TIMEOUT_SECS = 60

        def run(self):
            num_retry = 0
            while True:
                with self.cv:
                    was_notified = self.cv.wait_for(
                        lambda: self.should_stop or self.do_channel_change_now,
                        timeout=self.CHANGE_CHANNEL_RETRY_TIMEOUT_SECS
                    )
                if self.should_stop:
                    return
                if was_notified:
                    num_retry = 1
                elif num_retry > 0:
                    print(f'Retrying #{num_retry}: ', end='')
                    num_retry += 1
                self._cmd_change_channel.change_channel()
                self.do_channel_change_now = False

    def __init__(self, output_file, cmd_change_channel):
        self._recs = []
        self._output_file = output_file
        self._comp_re = re.compile(
            VideoStartTimeParser._re, flags=re.I | re.M | re.X)
        self.ch_change_th = None
        if cmd_change_channel:
            self.cv = threading.Condition()
            self.ch_change_th = VideoStartTimeParser.ChannelChangerThread(
                self.cv, cmd_change_channel)
            self.ch_change_th.start()

    def __del__(self):
        try:
            self._output_file.close()
        except OSError:
            pass  # fallthrough
        if self.ch_change_th and self.ch_change_th.is_alive():
            self._do_notify(should_stop=True)
            self.ch_change_th.join()

    def _do_notify(self, should_stop):
        with self.cv:
            if should_stop:
                self.ch_change_th.should_stop = True
            else:
                self.ch_change_th.do_channel_change_now = True
            self.cv.notify()

    def _notify_channel_changer(self, should_stop):
        if self.ch_change_th and self.ch_change_th.is_alive():
            self._do_notify(should_stop)

    def process(self, line):
        logging.debug(line if line[-1] != '\n' else line[:-1])
        m = self._comp_re.match(line)
        if m:
            if Global.args.should_output:
                num_recs = len(self._recs)
                print(
                    f'Appending record #{num_recs+1}'
                    f' in {self._output_file.name}:\n{line}')
                try:
                    self._output_file.write(line)
                    if num_recs % 5 == 0:
                        self._output_file.flush()
                except OSError:
                    pass  # fallthrough
            gd = m.groupdict()
            rec = VideoStartTimeRecord(gd)
            self._recs.append(rec)
            self._notify_channel_changer(should_stop=False)

    def get_records(self):
        return self._recs


class VideoStartTimeAnalyzer:
    """Analyzes the records obtained by the parser and provides a breakdown
    of the gathered video start time metrics.
    """

    _analysis_fields = ['render', 'licacq', 'dmxctor1',
                        'prebuffer', 'preroll', 'drmload', 'manparse']

    def __init__(self, parser):
        self._parser = parser

    def __getattr__(self, name):
        # All inexistent members will created as empty lists by default
        setattr(self, name, [])
        return getattr(self, name)

    def _add_custom_metric(self, record, metric, begin, end):
        begin_var, begin_field, begin_index = begin
        vbegin = int(getattr(record, begin_field).split('-')[begin_index])
        end_var, end_field, end_index = end
        vend = int(getattr(record, end_field).split('-')[end_index])
        duration = abs(vend - vbegin)
        getattr(self, metric).append(duration)
        logging.debug(f'{begin_var}={vbegin}, {end_var}={vend}'
                      f', {metric}={duration}')

    def analysis(self):
        print('\nAnalyzing...')
        records = self._parser.get_records()
        if not records:
            return 'No records found.'
        num_records = len(records)
        for i, r in enumerate(records, 1):
            logging.info(f'Processing record #{i}/{num_records}: {vars(r)}')
            for field in VideoStartTimeAnalyzer._analysis_fields:
                # Ingest every relevant field of a record into a list
                v = getattr(r, field)
                splitted = v.split('-')
                begin, end = int(splitted[0]), int(splitted[-1])
                duration = end - begin
                if field in {'render'}:
                    # Override for single value fields
                    duration = int(begin)
                getattr(self, field).append(duration)
                logging.debug(f'{field} start-end={v}, duration={duration}')
            # Calculate diff between licacq and prebuffer start
            self._add_custom_metric(
                r, 'diff_licacq_prebuffer',
                ('licacq_begin', 'licacq', 0),
                ('prebuffer_begin', 'prebuffer', 0))
            # Calculate first frame after unpause
            self._add_custom_metric(
                r, 'diff_first_frame_after_unpause',
                ('last_decpreroll', 'decpreroll', -1),
                ('render', 'render', 0))
            # Calculate diff decpreroll first and first done
            self._add_custom_metric(
                r, 'diff_decpreroll_first_to_first_done',
                ('decpreroll_first', 'decpreroll', 0),
                ('decpreroll_first_done', 'decpreroll', 1))
            # Calculate diff prebuff and preroll last samples
            self._add_custom_metric(
                r, 'diff_last_prebuff_preroll',
                ('prebuff_last', 'prebuffer', -1),
                ('preroll_last', 'preroll', -1))
            logging.info('')
        ret = '\n'
        if getattr(self, 'licacq', None):
            num_records = len(self.licacq)
            multiple_records = num_records > 1
            header = (f'Analysis of {num_records}'
                      f' sample{"s" if multiple_records else ""} (ms):')
            ret += f'{header}\n{"-" * len(header)}\n'
            for var in vars(self):
                if var.startswith('_'):
                    continue
                values = getattr(self, var)
                stdeviation = stdev(values) if multiple_records else 0.0
                ret += (f'\t{var.rjust(35)}: '
                        f'median={str(round(median(values))).ljust(5)}, '
                        f'mean={str(round(mean(values))).ljust(5)}, '
                        f'min={str(min(values)).ljust(5)}, '
                        f'max={str(max(values)).ljust(5)}, '
                        f'stdev={str(round(stdeviation)).ljust(5)}\n')
        return ret


class Global:
    """Holds arguments used by the script and initializes the logging system."""

    _serial_port_prefix = '/dev/tty'
    _default_serial_port = _serial_port_prefix + 'USB0'
    _cmd_channel_change_choices = {
        'PressBackSelect': PressBackSelect, 'PressLeft': PressLeft}

    def __init__(self):
        argp = argparse.ArgumentParser(
            prog='km.mp.play.start.det log parser',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            description='''Parses 'km.mp.play.start.det' logs and prints a
            breakdown of the video startup times. When running with an
            --input_file as a serial port like \'/dev/tty*\', it'll
            automatically change channels as per some policy specified with
            --cmd_change_channel. When running with an --input_file as a file,
            it'll make the analysis of its contents. The specified --output_file
            is always appended to. Press CTRL+C anytime to cancel.''')
        argp.add_argument('-v', '--verbose', action='count', default=0,
                          help='specify multiple times for extra verboseness.')
        argp.add_argument('input_file', type=str, nargs='?',
                          default=Global._default_serial_port,
                          help='''file containing the logs to parse.
                          If using the serial port, please make sure to exit
                          minicom/picocom firstly.''')
        argp.add_argument('--output_file', type=argparse.FileType('a'),
                          required=False,
                          default='/tmp/video_start_parsing_logs.txt',
                          help='''file that will have the parsed matching lines
                          appended to it.''')
        argp.add_argument('--ip_address', type=str, required=False,
                          default='10.15.20.1',
                          help='''IP address of the TV that will receive
                          the curl ECP commands''')
        argp.add_argument('--cmd_change_channel', required=False,
                          choices=Global._cmd_channel_change_choices,
                          default='PressLeft', help='''class defining the policy
                          describing the actions needed to play the next video.
                          Named by the very same actions it does.''')
        Global.args = argp.parse_args()
        # Setup logging
        log_levels = [logging.WARNING, logging.INFO, logging.DEBUG]
        log_level = log_levels[min(len(log_levels)-1, Global.args.verbose)]
        logging.basicConfig(level=log_level, format="%(message)s")
        Global.args.is_serial_port = Global.args.input_file.startswith(
            Global._serial_port_prefix)
        Global.args.should_output = Global.args.is_serial_port and (
            Global.args.input_file != Global.args.output_file.name)
        if not Global.args.should_output:
            msg = 'Will not output the parsed entries '
            if not Global.args.is_serial_port:
                msg += 'as the input is not a serial port.'
            else:
                msg += 'as the input and output are the same.'
            logging.warning(msg)


def main():
    Global()
    cmd_change_channel = None
    if Global.args.is_serial_port:
        cmd_change_channel = Global._cmd_channel_change_choices[
            Global.args.cmd_change_channel](Global.args.ip_address)
        channel_msg = (f'Start {cmd_change_channel.channel_name} now'
                       f' and then')
        sep = "-" * 20
        msg_len = max(len(channel_msg), 40)
        print(
            f'{sep} {"Close minicom now".center(msg_len)} {sep}\n'
            f'{sep} {channel_msg.center(msg_len)} {sep}\n'
            f'{sep} {"Please press [ENTER] to continue".center(msg_len)} {sep}',
            end='')
        input()
        print()
    parser = VideoStartTimeParser(Global.args.output_file, cmd_change_channel)
    try:
        with fileinput.input(Global.args.input_file,
                             openhook=fileinput.hook_encoded(
                                 "utf-8", "surrogateescape")) as f:
            for line in f:
                parser.process(line)
    except (KeyboardInterrupt, OSError):
        pass  # fallthrough
    # Always analyze even if interrupted above while processing input
    try:
        analyzer = VideoStartTimeAnalyzer(parser)
        print(analyzer.analysis())
    except (KeyboardInterrupt, OSError):
        pass  # fallthrough


if __name__ == '__main__':
    main()
