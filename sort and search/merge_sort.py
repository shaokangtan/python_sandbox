# best        average      worst
# O{nLog(n)) O{nLog(n)) O{nLog(n))
# strategy: divide and conquire, divide by 2 groups and log(n) steps, each step runs n elements.
#           total time complex is O(n * log(n))
#https://en.wikipedia.org/wiki/Merge_sort

o = 0
def exe_merge_sort(arr):
    global o
    if len(arr) <= 1:
        return 0
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    result = exe_merge_sort(left)
    result += exe_merge_sort(right)

    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        o += 1
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
        result += 1


    while i  < len(left):
        o+= 1
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        o += 1
        arr[k] = right[j]
        j += 1
        k += 1

    print ("arr {}".format(arr))
    print ("left {}".format(left))
    print("right {}".format(right))
    return result

def merge_sort(arr):

    if len(arr)>1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k]=lefthalf[i]
                i=i+1
            else:
                arr[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            arr[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            arr[k]=righthalf[j]
            j=j+1
            k=k+1
        print ("arr {}".format(arr))
        print ("lefthalf {}".format(lefthalf))
        print("righthalf {}".format(righthalf))

arr = [11,2,5,4,7,6,8,1,23]
#merge_sort(arr)
o=0
exe_merge_sort(arr)
print (arr)
print (o)
