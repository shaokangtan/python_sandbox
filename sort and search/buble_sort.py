# best average worst
# O{n) O(n^2) O(n^2)
def exe_binary_sort(arr):
    o = 0
    for i in range (len(arr)-1, 0, -1):
        for j in range (0, i):
            if arr[j] > arr[j+1]:
                o += 1
                tmp = arr[j]
                arr[j]= arr[j+1]
                arr[j+1]=tmp
    return o
def exe_binary_sort_improved(arr):
    
    o = 0
    for i in range (len(arr)-1, 0, -1):
        swapped = False
        for j in range (0, i):
            if arr[j] > arr[j+1]:
                o += 1
                #tmp = arr[j]
                #arr[j]= arr[j+1]
                #arr[j+1]=tmp
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break
    return o

'''
procedure bubbleSort( A : list of sortable items )
    n = length(A)
    repeat 
        swapped = false
        for i = 1 to n-1 inclusive do
            /* if this pair is out of order */
            if A[i-1] > A[i] then
                /* swap them and remember something changed */
                swap( A[i-1], A[i] )
                swapped = true
            end if
        end for
    until not swapped
end procedure
'''

def binary_sort (A):
    o = 0
    swapped = True
    while swapped :
        swapped = False
        for i in range (1,len(A)):
            o += 1
            # if this pair is out of order
            if A[i-1] > A[i]:
             # swap them and remember something changed
                tmp =  A[i-1]
                A[i-1] = A[i]
                A[i] = tmp
                swapped = True
    return o
arr = [20,13,8,7,6,5,4,3,2,1]
o = exe_binary_sort(arr)
print (arr)
print ("o = {}".format (o))
arr = [20,13,8,7,6,5,4,3,2,1]
o = binary_sort(arr)
print (arr)
print ("o = {}".format (o))
arr = [20,13,8,7,6,5,4,3,2,1]
o = binary_sort(arr)
print (arr)
print ("o = {}".format (o))
arr =  [20,13,8,7,6,5,4,3,2,1]
o = exe_binary_sort_improved(arr)
print (arr)
print ("o = {}".format (o))
arr = [3,2,13,4,6,5,7,8,1,20]
o = binary_sorts(arr)
print (arr)
print ("o = {}".format (o))

'''
arr = [1,2,3,4]
for n in range(len(arr)-1,0,-1):
    print (arr[n] )
    
for n in range(0, len(arr)):
    print (arr[n] )
'''


