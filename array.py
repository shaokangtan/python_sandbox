a = [0, 1, 2, 3, 4 ]

b = a #shallow copy


c = a.copy() #dynamic copy
d = a[:]

b[0] = 3


print ("a[] ={}".format(a))
print ("b[] ={}".format(b))
print ("c[] ={}".format(c))

a.extend([5,6,7])
print (a)



