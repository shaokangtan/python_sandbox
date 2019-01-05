#dutch flag question
def dutch_flag(arr,num):
    greater_equal_num_index = 0
    arr.insert(0,num)
    for i,v in enumerate(arr):
        if v >= num:
            if greater_equal_num_index == -1: 
                greater_equal_num_index = i
        else:
            if greater_equal_num_index != -1 :
                arr[i],arr[greater_equal_num_index] = arr[greater_equal_num_index], arr[i] 
                if greater_equal_num_index + 1 < len(arr)  and  arr[greater_equal_num_index + 1] >= num:
                    greater_equal_num_index += 1
                else:
                    greater_equal_num_index = -1 


arr = [1,3,5,7,9,8,6,4,2,0]

dutch_flag(arr, 8)
print (arr)

arr = [1,3,5,7,9,8,6,4,2,0]

dutch_flag(arr, -1)
print (arr)
