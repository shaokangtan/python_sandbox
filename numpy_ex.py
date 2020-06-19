import numpy

''' 
example input:
2 2
1 2
3 4

3 2
1 2
3 4
5 6
'''

array_1 = numpy.array([[1,2,3],[0,0,0],[4,5,6]])
array_2 = numpy.array([[0,0,0],[7,8,9],[10,11,12]])
array_3 = numpy.array([[13,0,0],[14,8,9],[1,11,12]])

print (numpy.concatenate((array_1, array_2, array_3), axis = 0))
print (numpy.concatenate((array_1, array_2, array_3), axis = 1))

print (numpy.concatenate((array_1, array_2, array_3, array_3), axis = 2))
exit(0)

row, col = map(int, input().split())
b = [ ]
for i in range (row):
    a = list(map(int, input().split()))
    b.append(a)
if len(a) != col:
    assert "error in col"
if len(b) != row:
    assert "error in row"

my_array = numpy.array(b)
print (numpy.transpose(my_array))

print (my_array.flatten())

print (numpy.concatenate(b))
