from collections import *
def number_needed(A,B):
    a = Counter(A)
    print (a)
    b = Counter(B)
    print (b)
    c = a - b
    print (c)
    d = b - a
    print (d)
    e = c + d
    return  len(list(e.elements()))


a = input().strip()
b = input().strip()

print(number_needed(a, b))
