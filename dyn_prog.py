r = 0
def find_sets(arr, total, i):
    global r
    r += 1
    if total == 0:
        print ("total: {}, i: {} found match set".format(total, i))
        return 1
    if total < 0:
        return 0
    if i < 0:
        return 0

    print ("total: {}, i: {}".format(total, i))
    # find mached total and total - arr[i]
    return find_sets(arr, total-arr[i], i-1) + find_sets(arr, total, i-1)


def find_sets_m(arr, total, i, memo):
    global r

    key = str(total) + ":" + str(i)
    if  key in memo:
        return memo[key]
    # find mached total and total - arr[i]
    r += 1


    if total == 0:
        return 1
    if total < 0:
        return 0
    if i < 0:
        return 0
    memo[key] = find_sets_m(arr, total-arr[i], i-1, memo) + find_sets_m(arr, total, i-1, memo)
    return memo[key]

#no duplicate, negative and zero element
match = 8
#a = [1, 2, 3 ,5 , 7 ,10, 13]
a = [1, 2, 3 ,5]
memo = {}

print (find_sets(a, match, len(a)-1))
print (r)

memo.clear()
r = 0
print (find_sets_m(a, match, len(a)-1, memo))
print (r)


r = 0
a.sort(reverse=1)
print (find_sets(a, match, len(a)-1))
print (r)

memo.clear()
r = 0
print (find_sets_m(a, match, len(a)-1, memo))
print (r)

