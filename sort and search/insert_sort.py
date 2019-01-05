# best average worst
# O(n) O(n^2) O(n^2)
# memory space O(1)
# stratgey: this is better algorith than selection sort and buble sort
#           each iteration take advanage of previous interation result when sorting the element
#           plus, when the condition is met, we shift the candidate one position up, instead of swaping the cadidates.
#           The bubble sort and selection sort swap the cadidates in when condition is met.
def exe_insertion_sort(arr):
    o = 0
    for i in range (1, len(arr)):
        position = i-1
        current_value = arr[i]
        print ("iteration: {}, current value: {} shifting - ".format(i, current_value), end="")
        while position >= 0 and  current_value < arr[position]:
            o += 1
            print ("{} ".format(arr[position]), end="")
            arr[position+1] = arr[position] # shifting larger element to right
            position = position -1
        print ("")
        arr[position+1]=current_value # update the result !!!
    return o

def insertion_sort(arr):

    # For every index in array
    for i in range(1,len(arr)):

        # Set current values and position
        currentvalue = arr[i]
        position = i
        # Sorted Sublist
        while position>0 and arr[position-1]>currentvalue:

            arr[position]=arr[position-1]
            position = position-1

        arr[position]=currentvalue

arr =[3,5,4,6,8,1,2,12,41,25]
print (arr)
#insertion_sort(arr)
o = exe_insertion_sort(arr)
print (arr)
print ("o = {}".format (o))