def number_needed(A, B):
    a = list(A)
    b = list(B)
    ans = 0
    for i in range(len(a)):
        for j in range (len(b)):
            if a[i] == b[j]:
                a[i]=0
                b[j]=0
                break
    for i in range(len(a)) :
        if a[i] != 0:
            ans +=1
    for j in range(len(b)) :
        if b[j] != 0:
            ans +=1
    return ans

a = input().strip()
b = input().strip()

print(number_needed(a, b))
