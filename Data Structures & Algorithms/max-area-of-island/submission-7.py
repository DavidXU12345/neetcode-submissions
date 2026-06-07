class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(row, col):
            if not (0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 1):
                return 0
            grid[row][col] = 0
            area = 1
            for d in directions:
                new_row = row + d[0]
                new_col = col + d[1]
                area += dfs(new_row, new_col)
            return area

        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                max_area = max(dfs(r, c), max_area)
        return max_area

