
from collections import deque
deadends = ["0201","0101","0102","1212","2002"]
target = "0202"

def openLock(deadends, target):
    marker, depth = 'x', 0
    visited, q, deadends = set(), deque(['0000', marker]), set(deadends)

    while q:
        node = q.popleft()
        if node == target:
            return depth  # found
        if node in visited or node in deadends:
            continue # return if 1. already tried or 2. this is a deadend
        if node == marker and not q:
            return -1 # fail to found solution
        if node == marker:
            q.append(marker)
            depth += 1
        else:
            visited.add(node)
            q.extend(successors(node))
    return -1

def successors(src):
    res = []
    for i, ch in enumerate(src):
        num = int(ch)
        res.append(src[:i] + str((num - 1) % 10) + src[i+1:])
        res.append(src[:i] + str((num + 1) % 10) + src[i+1:])
    return res

num = openLock(deadends,target)
print (num)