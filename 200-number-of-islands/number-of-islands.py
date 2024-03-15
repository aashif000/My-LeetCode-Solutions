class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        island = 0
        def dfs(i,j):
            if i not in range(rows) or j not in range(cols) or grid[i][j]=='0' or (i,j) in visited:
                return 
            visited.add((i,j))
            d = [[0,1],[0,-1],[1,0],[-1,0]]
            for dr,dc in d:
                dfs(i+dr, j+dc)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1' and (i,j) not in visited:
                    dfs(i,j)
                    island+=1
        return island