#sort the random number into valley and peak pattern
def peak_valley(arr):
    flag = 0 # 0 valley else peak

    for i in range(len(arr)-1) :
        if flag == 0:
            if arr[i]>arr[i+1]:
                arr[i], arr[i+1] = arr[i+1],arr[i]

        else:
            if arr[i]<arr[i+1]:
                arr[i], arr[i+1] = arr[i+1],arr[i]
        flag = ~flag


def validate_peak_valley(arr):
    flag = 0 # 0 valley else peak

    for i in range(len(arr)-1) :
        if flag == 0:
            if arr[i]>arr[i+1]:
                print ("Error at {}: {}".format(i, arr[i]))
                return False

        else:
            if arr[i]<arr[i+1]:
                print ("Error at {}: {}".format(i, arr[i]))
                return False
        flag = ~flag

    return True
array = [1,2,3,4,5]
array1 = [1,1,2,3,3,4,5]
array2 = [5,4,3,2,1]
import random


peak_valley(array)
print(validate_peak_valley(array))
peak_valley(array1)
print(validate_peak_valley(array1))
peak_valley(array2)
print(validate_peak_valley(array2))


random_array = [random.randint(0,1000) for x in range(1000)]
peak_valley(random_array)
print(validate_peak_valley(random_array))
print (random_array)