a=[4,3,1,2]
b=[2,3,4,1]
c=[a[:],b[:]]
#enumerate 2 dimensional array
d = [(key, i) for i, key in enumerate(c[0])] # map list to tuple
print (d)
# enumerate list to tuple list
d = [(key, i) for i, key in enumerate(a)] # map list to tuple
print (d)
# enumerate list to map
d = {key: i for key, i in enumerate(a)} # map list to dictionary
print (d)
# enumerate list to set
d = set( i for key, i in enumerate(a)) # map list to set
print (d)

#enumerate map to set
food = [ ("apple", 7), ("banana", 3), ("lemon", 8), ("orange", 3), ("kiwi", 2), ("apple", 1), ("banana", 2), ("lemon", 3), ("orange", 4) , ("kiwi", 5)]
d = set( (key, i) for key, i in enumerate(food)) # map tupple list to set
print (d)
d = set( i for key, i in enumerate(food)) # map tupple  to set
print (d)
d = set( i[0] for key, i in enumerate(food)) # map grocery to set
print (d)