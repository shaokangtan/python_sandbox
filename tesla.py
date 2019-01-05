import math



def solution(A, B):
    # write your code in Python 3.6
    total = 0
    if A > 0:
        total = math.sqrt(B) - math.sqrt(A)
        return total  + 1
    else:
        if A < 0 :
            return 0
    """
    for i in range (A,B,1):
        n = abs(i)
        if n**0.5 == int(n**0.5):
            total += 1"""
    return int(total) +1


total = solution (4, 17)
total = solution (-1000, 500)
print (total)


#A = [40,40,100,80,20]
#B = [3,3,2,2,3]
A = [60,80,40]
B= [2,3,5]
"""
A[0] =  40    B[0] = 3
A[1] =  40    B[1] = 3
A[2] = 100    B[2] = 2
A[3] =  80    B[3] = 2
A[4] =  20    B[4] = 3
"""

def solution(A, B, M, X, Y):
    # write your code in Python 3.6
    exit_floors = {}
    total_weight = 0
    total_stops = 0
    total_people = 0
    for index in range(0,len(A), ):
        if (total_weight + A[index] <= Y) and (total_people < X) : # < max_weight
            exit_floors[B[index]] = 1 # floor to exit, note we may exit on the same floor
            total_weight += A[index]
            total_people += 1
        else:
            total_stops += len(exit_floors)  # total stop
            total_stops += 1 # return to ground
            exit_floors.clear()
            exit_floors[B[index]] = 1
            total_weight = A[index]
            total_people = 1

    total_stops += len(exit_floors)  # total stop
    total_stops += 1 # return to ground
    return total_stops

#n = solution(A,B,3,5 ,200)
n = solution(A,B,5,2,200)
print (n)

exit(0)

def solution(A):
    dic = {}
    # write your code in Python 3.6
    for i in range(0,len(A)):
        if A[i] > 0:
            dic[A[i]] = 1

    for i in range(1,1000000):
        if i in dic:
            continue
        else:
            return i



num = 256
bin_str = str(bin(num))
import re
ptrn = re.compile("0+")
max = 0
matches = re.finditer(ptrn, bin_str[2:])
for matchNum, match in enumerate(matches):
    print ("{} {} ".format(match.end()- match.start(), match.group()))
    #l = len(m)
    #if l > max:
    #    max = l
c=0
while num:
    if (num%2)==0:
        c = c + 1
        if c > max:
            max = c
    else:
        c = 0
    num = num // 2

print (max)

#arr=[1, 3, 6, 4, 1, 2]
#arr=[1]
#arr=[-1]
arr=[-1, -5, 3]

print (solution(arr))