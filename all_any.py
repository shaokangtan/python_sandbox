
# exercise all and any
'''
#test = "123454321"

test = "1234567890"

print (test[::-1])

exit(0)

'''

def reverse_str(j):
    l = len(j)
    tmp = ""
    for i in range(l, 0, -1):
        tmp += j[i-1]
    print (tmp)
    return tmp

N,n = int(input()),input().split()
#print  all ([int(i)>0 for i in n]) and any([j == j[::-1] for j in n])
print  (all ([int(i)>0 for i in n]) and any([j == reverse_str(j) for j in n]))
