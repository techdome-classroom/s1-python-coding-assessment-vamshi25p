class Solution:

    def getTotalIsles(self, grid: list[list[str]]) -> int:
        #    write your code here
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 'W' or (r, c) in visited):
                return
            visited.add((r, c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'L' and (i, j) not in visited:
                    dfs(i, j)
                    count += 1
        return count
