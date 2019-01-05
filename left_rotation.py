def array_left_rotation(a, n, k):
    l = k
    while k:
        tmp = a.pop(0)
        a.append(tmp)
        k = k - 1
    return a


n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
