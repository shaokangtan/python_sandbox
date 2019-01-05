def findCircleNum(A):
    N = len(A)
    seen = set()
    def dfs(node):
        for nei, adj in enumerate(A[node]):
            if adj and nei not in seen:
                seen.add(nei)
                dfs(nei)

    ans = 0
    for i in range(N):
        if i not in seen:
            dfs(i)
            ans += 1
    return ans

def findCircleNum_1(M):
    """
    :type M: List[List[int]]
    :rtype: int
    """
    if len(M) == 0: return 0
    s = set(range(len(M)))
    count = 0
    q = []
    while True:
        if len(q) == 0:
            if s:
                q.append(s.pop())
                count += 1
            else:
                break
        item, q = q[0], q[1:]
        for i in list(s):
            if M[item][i]:
                q.append(i)
                s.remove(i)
    return count


A = [[1,1,0],
 [1,1,1],
 [0,1,1]]
print (findCircleNum(A))

A = [[1,1,0],
 [1,1,0],
 [0,0,1]]
print (findCircleNum(A))

print (findCircleNum_1(A))