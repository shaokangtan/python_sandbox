#exercise time module
import time
time_sec = time.time() #Return the current time in seconds since the Epoch.
print ("{} is {}".format(time_sec, time.ctime(time_sec )  ) )
time_cpu = time.clock() #Return the CPU time or real time since the start of the process or since the first call to clock()
time.sleep(0.5)
new_time_cpu = time.clock() #Return the CPU time or real time since the start of the process or since the first call to clock()
print ("past cpu time is {}, new cpu time is {}".format(time_cpu, new_time_cpu) )
time_tuple = time.localtime(time_sec) #Convert seconds since the Epoch to a time tuple expressing local time.
print (time_tuple)
time_sec_1 = time.mktime(time_tuple) #Convert a time tuple in local time to seconds since the Epoch.
print (time_sec_1)
print (time.asctime((2018,12,8,0,0,0,0,0,0)))



