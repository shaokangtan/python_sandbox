import pytz
import datetime

#print all time zones in sorted order
print ("{0} zones".format(len(pytz.all_timezones_set)))
zones = []
for obj in pytz.all_timezones_set:
    zones.append (obj)
#help(pytz.timezone)
sorted(zones)
print (zones)

#print Moscow time zone in local time
country = 'Europe/Moscow'

tz_to_display = pytz.timezone(country)

local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {} is {}".format(country, local_time))
print("UTC is {}".format(datetime.datetime.utcnow()))

# for x in pytz.all_timezones:
#     print(x)
#
# for x in sorted(pytz.country_names):
#     print(x + ": " + pytz.country_names[x])
#
for x in sorted(pytz.country_names):
    print("{}: {}".format(x, pytz.country_names[x]), end=': ')
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t\t{}: {}".format(zone, local_time))
    else:
        print("\t\tNo time zone defined")
