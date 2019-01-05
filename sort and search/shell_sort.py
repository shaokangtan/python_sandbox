# best average worst
# O{nLog(n)) O{nlogn) O{Log(n^2)}
# strategy: divide the candidate list into groups of evened gap,
#           use insertion sort to sort each group
#           change the gapped group size fom n/2, n/4, ....2. where n is the size of candidate list
# https://en.wikipedia.org/wiki/Shellsort
# notes: 2/9 -Henry Tan
def shell_sort(arr):
    sublistcount = len(arr)//2

    # While we still have sub lists
    while sublistcount > 0:
        for start in range(sublistcount):
            # Use a gap insertion
            gap_insertion_sort(arr,start,sublistcount)
            print ("sublistcount : {}" .format (sublistcount))
            print ("arr : {}".format (arr))

        sublistcount = sublistcount // 2

def gap_insertion_sort(arr,start,gap):
    for i in range(start+gap,len(arr),gap):

        currentvalue = arr[i]
        position = i

        # Using the Gap
        while position>=gap and arr[position-gap]>currentvalue:
            arr[position]=arr[position-gap]
            position = position-gap

        # Set current value
        arr[position]=currentvalue

arr = [45,67,23,45,21,24,7,2,6,4,90]
shell_sort(arr)
print (arr)