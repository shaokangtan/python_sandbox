#
# 1. how to convert list to dictionary using iterator
#
# 2. how to sort dictionary by value or key
#
a=[4,3,1,2]
b=[2,3,4,1]
x=5
d = {key: i for i, key in enumerate(a)} # map list to dictionary

my_dict = {1:"123", 2:"234"}

for i in a:
    if d[x-i] != None:
        print ("{} {}". format(i, x-i))


# sort dictionary by value
dict = {1: 2, 2: 10, 3: 7, 4:5}

sorted_dict = sorted(dict, key=dict.get)

print (sorted_dict)

# sort dictionary by key
dict = {10: 2, 2: 10, 3: 7, 1:5}

sorted_dict = sorted(dict.items())

print (sorted_dict)