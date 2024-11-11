class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visited=set()
        def dfs(r,c):
            if(r<0 or c<0 or r>=rows or c>=cols or grid[r][c]=='W' or (r,c) in visited):
                return
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
                    
        return 0
