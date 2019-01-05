if __name__ == '__main1__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    arr = []
    for i in range (x + 1):
        for j in range (y + 1):
            for k in range (z + 1):
                if (i + j + k) != n:
                    arr.append ([i,j,k])

    print (arr)

if __name__ == '__main2__':
    n = int(input())
    arr = list(map(int, input().split()))
    c = -101
    r = -101
    #print (arr)
    #print (arr[0])
    for s in arr:
        if s > c:
            r = c
            c = s
        elif s < c:
            if s > r:
                r = s
    #print(c)
    print(r)

if __name__ == '__main3__':
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if arr == []:
            arr.append([name,score])
            #print (arr[0][0])
        else:
            insert = len(arr)
            for i in range(len(arr)):
                if arr[i][1] <  score:
                    continue
                else:
                    if arr[i][1] == score:
                        if arr[i][0] < name:
                            continue
                        else:
                            insert = i
                            break;
                    else:
                        insert = i
                        break
            arr.insert(insert,[name,score])
    print (arr)
    l = arr[0][1]
    for i in range(1, len(arr)):
        if arr[i][1] == l:
            continue;
        else:
            l = arr[i][1]
            print (arr[i][0])
            break;

    for j in range(i + 1, len(arr)):
        if arr[j][1] == l:
            print (arr[j][0])
        else:
            break;

if __name__ == '__main4__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    sum =0
    for i  in range (len(student_marks[query_name])):
        sum += student_marks[query_name][i]
    sum /=3
    print("%.2f" % sum)
    print("%.2f" % round(sum,2))
    print ("{0:.2f}".format(sum))

if __name__ == '__main5__':

    #Replace all ______ with rjust, ljust or center.

    thickness = int(input()) #This must be an odd number
    c = 'H'

    #Top Cone
    for i in range(thickness):
        print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

    #Top Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

    #Middle Belt
    for i in range((thickness+1)//2):
        print((c*thickness*5).center(thickness*6))

    #Bottom Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
    
    #Bottom Cone
    for i in range(thickness):
        print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

    for i in range(40):
        print("%d"%(i%10), end="")


if __name__ == "__main__":
    #!/bin/python3

    import sys

    def countInversions(arr):
        # Complete this function
        if len(arr) <= 1:
            return 0
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        result = countInversions(left)
        result += countInversions(right)

        i = 0
        j = 0
        k = 0
        while i<len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
                result += 1
            k += 1


        while i  < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        return result


    arr = [1,1,1,2,2]
    result = countInversions(arr)
    print (arr)
    print (result)
    arr = [2,1,3,1,2]
    result = countInversions(arr)
    print (arr)
    print (result)
'''
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = countInversions(arr)
        print ()
        print(result)
        print (arr)

'''