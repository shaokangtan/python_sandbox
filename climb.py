def climb(arr):
    if len(arr) < 2:
        return 0

    min = arr[0]
    max = 0

    for i in range (1, len(arr), 1):
        if arr[i-1] > arr[i]:
            # downhill
            # do nothing here
            pass
        else:
            # up hill
            if max < arr[i]:
                max = arr[i]
            if min > arr[i-1]:
                min = arr[i-1]
            print ( "current climb {}". format(max - min) )
    if max - min < 0:
        return 0
    else:
        return max - min


if __name__ == "__main__":
    climbs = [15, 4, 7, 5, 12, 0]
    print (climb(climbs))

