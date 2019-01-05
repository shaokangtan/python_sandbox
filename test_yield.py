def my_yield(n: int):
    start = 0
    while start < n:
        print("start = {}".format(start))
        yield start
        start += 1


y = my_yield(5s)
print (y)


for i in y:
    print("loop = {}".format(i))
