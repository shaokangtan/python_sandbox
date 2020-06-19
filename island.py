def numIslands(grid):
    if not grid:
        return 0

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1
    return count

def dfs(self, grid, i, j):
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
        return
    grid[i][j] = '#'
    self.dfs(grid, i+1, j)
    self.dfs(grid, i-1, j)
    self.dfs(grid, i, j+1)
    self.dfs(grid, i, j-1)
def numIslands1(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    def sink(i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
            grid[i][j] = '0'
            map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
            return 1
        return 0
    return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))

g1 = [
    ['1','1','1','1','0'],
    ['1','1','0','1','0'],
    ['1','1','0','0','0'],
    ['0','0','0','0','0']]
lis = [(i,j) for i in range(3) for j in range(2)]

print (lis)


result = numIslands(g1)
print (result)
