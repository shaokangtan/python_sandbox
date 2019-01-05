
'''
The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ... The next number is found by adding up the two numbers before it.
'''
""" Big O calcuation
https://stackoverflow.com/questions/360748/computational-complexity-of-fibonacci-sequence
"""

"""if your comipler runs out of stack limit(maximum recursion depth exceeded in comparison), 
you can use for loop"""
def fibonacci(n):
    sum0=0
    sum1=1
    for i in range(min(2,n)):
        return 1
    for i in range(2,n):
        sum = sum0 + sum1
        sum0 = sum1
        sum1 = sum
        return sum

def fibonacci_n(n, memo):
    global r
    sum0=0
    sum1=1
    if n in memo:
        return memo[n]
    start = len(memo)
    if start-1 in memo:
        sum1 = memo[start - 1]
        sum0 = memo[start - 2]
    else:
        start = 2
    for i in range(start,n+1):
        sum = sum0 + sum1
        sum0 = sum1
        sum1 = sum
        r += 1
        memo[i] = sum

    return memo[n]


def fibonacci_r(n):
    if n < 2:
        return n
    else:
        total = fibonacci_r(n - 2) + fibonacci_r(n - 1)
        return total;

def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)


"""Fabonacci time complexity is O(2^N)
you can use memoization and dynamic programming to lower time complexity to O(N)"""
r = 0
def fibonacci_r_n(n,memo):
    global r
    if n in memo:
        return memo[n]
    if n <= 2 :
        memo[n] = 1
    else:
        r += 1
        memo[n] = fibonacci_n(n-1,memo) + fibonacci_n(n-2,memo)
    return memo[n]



#fibonacci(6)

#for i in range(6):
#    print ("{} ".format(fibonacci_r(i)))

#fib(5)

memo = {0:0, 1:1}
r = 0
for i in range(10, 0, -1):
    r = 0
    print ("{}: {}".format(i, fibonacci_n(i, memo)))
    #print (r)
print ("{}: {}".format(i, fibonacci_n(11, memo)))

def fab_python(n):
    a = 0
    b = 1
    for i in range(n):
        a,b = b, a+b
    return a

for i in range(10):
    print ("{}:{}".format(i,fab_python(i)))