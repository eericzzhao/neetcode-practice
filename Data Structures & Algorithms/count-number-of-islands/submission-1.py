class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0], [-1,0], [0, 1], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        numIslands = 0

        def dfs(r, c):
            # Case that our row or column is negative OR that our row or column is greater than the allowed amount of rows and columns OR that we've touched water
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or grid[r][c] == "0"):
                return 
            
            grid[r][c] = "0"
            # This seaprates the row and column movement
            for rowDirection, colDirection in directions:
                dfs(r + rowDirection, c + colDirection)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r,c)
                    numIslands += 1
        return numIslands



        