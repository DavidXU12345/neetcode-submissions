class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(row, col, visited):
            max_length = 1
            # visited.add((row, col))
            for row_d, col_d in DIRS:
                new_row = row + row_d
                new_col = col + col_d
                if 0 <= new_row < ROWS and 0 <= new_col < COLS and (new_row, new_col) not in visited and matrix[new_row][new_col] > matrix[row][col]:
                    max_length = max(max_length, 1 + dfs(new_row, new_col, visited))
            return max_length

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c, set()))
        return res