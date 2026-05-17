class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        def dfs(row, col):
            if not (0 <= row < ROW and 0 <= col < COL):
                return
            if grid[row][col] == '0':
                return
            # print(f"dfs {row} {col}")
            grid[row][col] = '0'
            dfs(row, col + 1)
            dfs(row, col - 1)
            dfs(row + 1, col)
            dfs(row - 1, col)
        
        count = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == '1':
                    # print(r, c)
                    dfs(r, c)
                    count += 1
        
        return count