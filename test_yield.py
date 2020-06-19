def my_yield(n):
    start = 0
    while start < n:
        print("start = {}".format(start))
        yield (start, 1)
        start += 1


y = my_yield(5)
print(y)



for i,j in y:
    print("loop = {}".format(i))
