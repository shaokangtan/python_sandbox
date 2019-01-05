names = ('Jack', 'Jill', 'Steve')
result = list(filter(None, names))
print (result)

result = list(filter(lambda x: x != 'Jill', names))
print (result)