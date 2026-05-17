class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        maxArea = 0

        def dfs(row, col, currentArea):
            nonlocal maxArea
            if (not (0 <= row < ROW and 0 <= col < COL)) or (grid[row][col] == 0):
                maxArea = max(maxArea, currentArea)
                return
            grid[row][col] = 0
            # print(row, col, currentArea)
            dfs(row, col + 1, currentArea + 1)
            dfs(row, col - 1, currentArea + 1)
            dfs(row + 1, col, currentArea + 1)
            dfs(row - 1, col, currentArea + 1)
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    dfs(r, c, 0)
        return maxArea