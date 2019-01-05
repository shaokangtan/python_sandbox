'''

Your task is to sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
'''


def my_sort(sample):
    even = []
    odd = []
    upper = []
    lower = []
    for i in sample:
        if i.isdigit():
            if int(i)%2:
                odd.append(i)
            else:
                even.append(i)
        if i.isupper():
            upper.append(i)
            continue
        if i.islower():
            lower.append(i)
            continue

    even.sort()
    odd.sort()
    lower.sort()
    upper.sort()
    tmp =""
    for i in lower:
        tmp += i
    for i in upper:
        tmp += i
    for i in odd:
        tmp += i
    for i in even:
        tmp += i
    return tmp

sample = input().strip()
print (my_sort(sample))

print(*sorted(sample, key=lambda c: (-ord(c) >> 5, c in '02468', c)), sep='')

# key sort three times
#1. c is lower = -1, c is digit = 1 else 0
#2. c is even even = 1 else = 0
#3. sort in ascii order
#example: Sorting1234

def inspect(c):
    if  c.islower():
        return 0
    if c.isupper():
        return 1
    if c.isdigit():
        if int(c)%2:
            return 2
        else:
            return 3

def inspect1(c):
    if  c.islower():
        return ord(c)
    if c.isupper():
        return 0x100 + ord(c)
    if c.isdigit():
        if int(c)%2:
            return 0x200 + ord(c)
        else:
            return 0x400 + ord(c)

print(*sorted(sample, key=lambda c: (inspect(c), c)), sep='')
print("inspect1")
print(*sorted(sample, key=lambda c: inspect1(c)), sep='')
print(*sorted(sample, key=lambda c: (c.isdigit() - c.islower())), sep='')
print(*sorted(sample, key=lambda c: (c.isdigit() - c.islower(), c in '02468')), sep='')
print(*sorted(sample, key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')

order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
print(*sorted(sample, key=order.index), sep='')

import string
print(*sorted(sample, key=(string.ascii_letters + '1357902468').index), sep='')