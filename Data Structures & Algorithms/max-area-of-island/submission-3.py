class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        maxArea = 0

        def dfs(row, col):
            if (not (0 <= row < ROWS and 0 <= col < COLS)) or (grid[row][col] == 0):
                return 0
            grid[row][col] = 0
            # print(row, col, currentArea)
            return 1 + dfs(row, col + 1) + dfs(row, col - 1) + dfs(row + 1, col) + dfs(row - 1, col)
        
        for r in range(ROWS):
            for c in range(COLS):
                maxArea = max(maxArea, dfs(r, c))
        return maxArea