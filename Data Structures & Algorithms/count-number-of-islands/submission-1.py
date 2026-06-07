class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(row, col):
            grid[row][col] = '0'

            for d in directions:
                new_row = row + d[0]
                new_col = col + d[1]
                if 0 <= new_row < ROWS and 0 <= new_col < COLS and grid[new_row][new_col] == '1':
                    dfs(new_row, new_col)

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    dfs(r, c)
                    res += 1
        return res
