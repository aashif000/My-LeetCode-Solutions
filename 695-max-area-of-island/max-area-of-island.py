class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        island = 0
        def dfs(i,j):
            if i<0 or j<0 or i==rows or j==cols or grid[i][j]==0 or (i,j) in visited:
                return 0
            visited.add((i,j))
            d = [[0,1],[0,-1],[1,0],[-1,0]]
            return 1+dfs(i,j+1)+dfs(i,j-1)+dfs(i+1,j)+dfs(i-1,j) 
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1 and (i,j) not in visited:
                    island = max(island,dfs(i,j))
        return island