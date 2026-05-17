class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False] * 10 for _ in range(9)]
        cols = [[False] * 10 for _ in range(9)]
        squares = [[False] * 10 for _ in range(9)]

        for col in range(9):
            for row in range(9):
                if board[row][col] == '.':
                    continue
                num = int(board[row][col])
                if rows[row][num] or cols[col][num] or squares[row // 3 * 3 + col // 3][num]:
                    return False
                rows[row][num] = True
                cols[col][num] = True
                squares[row // 3 * 3 + col // 3][num] = True
        return True
        