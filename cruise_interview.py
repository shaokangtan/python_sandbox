#question: find the time when h, m, s all align on the same tick
seconds = 24 * 60 * 60

def hand_sec(sec):
    tick = sec % 60
    return tick    
def hand_min(sec):
    min = sec // 60
    tick = min % 60 
    return tick 
def hand_hour(sec): 
    min = sec // 60
    hr = min // 60 
    tick = hr % 12
    return tick * (60//12)
import time
for sec in range(0,seconds,1):
    s = hand_sec(sec) 
    m = hand_min(sec)
    h = hand_hour(sec)
    #print ("{}:{}:{}".format(h,m,s))
    if (s== m) and  (m == h):
    #if  (hand_sec(sec) == hand_hour(sec)):
        print (time.strftime('%H:%M:%S', time.gmtime(sec)))
        
    

