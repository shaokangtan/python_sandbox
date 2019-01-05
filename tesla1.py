def solution(grid):
    if not grid:
        return 0
    paths = []
    path = []

    dfs(grid,paths,path,0,0)
    count = len(paths)
    print (count)
    for path in paths:
        cost = 0
        for step in path:
            i,j = step
            cost += grid[i][j]
        print (path)
        print (cost)

def dfs(grid, paths, path, i, j):
    if i==len(grid) or j==len(grid[0]):
        return
    #dynamic programming
    for p in paths:
        if (i,j) in p:
            index = p.index((i,j))
            path.extend(p[index:])
            paths.append(path);
            return
    #
    path.append((i,j))
    if (i == len(grid)-1 and j == len(grid[0])-1):
        # congratulation!
        paths.append(path);
        return
    new_path = path[:]
    l = len(paths)
    dfs(grid, paths, path, i+1, j)
    dfs(grid, paths, new_path, i, j+1)
    # memoization
    if len(paths) > l:
        mem[]
g = [ [1,1,1],[1,1,1],[1,1,1]]
g1 = [
    ['1','1','1','1','1'],
    ['1','1','1','1','1'],
    ['1','1','1','1','1'],
    ['1','1','1','1','1']]
#lis = [(i,j) for i in range(3) for j in range(2)]

#print (lis)


result = solution(g)
print (result)