def check_complete_circular_arrary(arr,start):
    total = len(arr)
    check_arr = [0] * total
    '''for i in range(len(array)):
        c = arr[i]
        if check_arr[i + c]:
            return False
        else:
            check_arr[i + c] = 1
    return True
    '''
    for i in range(len(arr)):
        c = arr[start]
        start = (start + c) % total
        if check_arr[start]:
            return False
        else:
            check_arr[start] = 1

    return True


def test_check_complete_circular_arrary():
    test_array = [2,2,-1]
    print ("{}".format(check_complete_circular_arrary(test_array, 0)))

import random

def create_circular_rel_idx_arrary(size, distance):
    arr= [0] * size
    c = 0
    r = []
    for i in range(size):
        if i == (size-1):
            arr[c] = 0 - c
            break
        d = random.randint(1, abs(distance))
        if d % 2:
            d = -d

        r.append(d)
        n = (c + d) % size
        while arr[n] !=0 or n == c:
            if d > 0:
                d = d + 1
            else:
                d = d - 1
            n = (c + d) % size

        arr[c] = d

        c = n % size
    return arr


#arr = create_circular_rel_idx_arrary(10, 3)

for i in range (100):
    arr = create_circular_rel_idx_arrary(1000, 10)
    if check_complete_circular_arrary(arr, 0):
        print ("True")
    else:
        print ("False")

#<class 'list'>: [-1, 2, -9, -9, 0, -5, 8, 2, 2, 4, -3, -3]