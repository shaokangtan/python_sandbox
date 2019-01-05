# best average worst
# O{nLog(n)) O{nLog(n)) O{n^2))
# use pivot to divide and conqure
# https://en.wikipedia.org/wiki/Quicksort
o = 0
def quick_sort(arr):

    quick_sort_help(arr,0,len(arr)-1)

def quick_sort_help(arr,first,last):

    if first<last:
        splitpoint = partition(arr,first,last)

        quick_sort_help(arr,first,splitpoint-1)
        quick_sort_help(arr,splitpoint+1,last)


def partition(arr,first,last):
    global o
    pivotvalue = arr[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
            o += 1

        while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1
            o += 1

        if rightmark < leftmark:
            done = True
        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp

    temp = arr[first]
    arr[first] = arr[rightmark]
    arr[rightmark] = temp

    return rightmark

o = 0
arr = [20,13,8,7,6,5,4,3,2,1]
quick_sort(arr)
print (arr)
print ("o = {}".format (o))
arr = [1, 2, 3, 4, 5, 6, 7, 8, 13, 20]
quick_sort(arr)
print (arr)
print ("o = {}".format (o))
arr = [3,2,13,4,6,5,7,8,1,20]
quick_sort(arr)
print (arr)
print ("o = {}".format (o))
