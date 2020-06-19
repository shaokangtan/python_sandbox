import sys, os
def test():
    print("hello")

test()
print(sys.executable)

# print ("test {}".format(None))
#
# detail_title='Godzilla: King of the Monsters'
# movies = ['Avengers:\nEndgame\n\nAPR 26 / PG-13\nACTION\n\n \n\n \n\nJoe Russo, Robert Downey,\nJr., Chris Evans, Josh Brolin\n\nIn theaters now, Pre-Order\n\nToday, Get A $3 Credit On\nRelease. Full details at ww\n\n***** A95%\nPRE-ORDERED UHD', "Us\n\nMAR 22 / R / 117 MIN\nCRIME & THRILLERS\n\n \n\n \n\nJordan Peele, Lupita\nNyong'o, Winston Duke,\n\nIn theaters now, pre-order\n\ntoday and get A $3 Credit\nOn Release. Full details at\n\n**** * D. 94%\nPRE-ORDERED UHD"]
# print len(movies)

import re
import time

counter_pattern = '(\d+):(\d+)'
ads_pattern_of = 'Ad(\d+)of(\d+)'
ads_pattern_0f = 'Ad(\d+)0f(\d+)'

ads_match = re.search(ads_pattern_of, 'Ad20f2'  )
if ads_match == None:
    ads_match = re.search(ads_pattern_0f, 'Ad20f2'  )
counter_match  = re.search(counter_pattern, '00:14')

print  ads_match.group(1),ads_match.group(2) , counter_match.group(1), counter_match.group(2)
t = time.clock()

time.sleep(2)

t1 = time.clock()

print time.clock()

print int(time.clock())

print t1-t
print int(t1-t)
