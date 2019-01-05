# best average worst
# O{n^2) O(n^2) O(n^2)
def exe_selection_sort(arr):
    for i in range( len(arr), 0, -1):
        max_pos = 0
        for j in range (0, i):
            if arr[j] > arr[max_pos]:
               max_pos = j
        tmp = arr[j]
        arr[j] = arr[max_pos]
        arr[max_pos]= tmp

def selection_sort(arr):

    # For every slot in array
    for fillslot in range(len(arr)-1,0,-1):
        positionOfMax=0

        # For every set of 0 to fillslot+1
        # find the largest element and swap it with the fillslot
        for location in range(1,fillslot+1):
            # Set maximum's location
            if arr[location]>arr[positionOfMax]:
                positionOfMax = location

        temp = arr[fillslot]
        arr[fillslot] = arr[positionOfMax]
        arr[positionOfMax] = temp



arr = [3,5,2,7,6,8,12,40,21]
#selection_sort(arr)
exe_selection_sort(arr)
print (arr)