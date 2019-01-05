C = [(a, b) for a in range(5) for b in range(3)]
print (C)

A = [[i for i in range (5)] for j in range (3)]
print (A)

a = list("12345")
print (a)

def convert(n):
    return   int(n)*10
    return n * 10

b = list(map(convert, a))
print (b)