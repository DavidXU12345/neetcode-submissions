class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if self.isSafe(r, c, board):
                    board[r][c] = 'Q'
                    backtrack(r + 1)
                    board[r][c] = '.'
              
        backtrack(0)
        return res

    def isSafe(self, r, c, board):
        n = len(board)
        row = r - 1
        while row >= 0:
            if board[row][c] == 'Q':
                return False
            row -= 1
        
        row = r - 1
        col = c - 1
        while row >= 0 and col >= 0:
            if board[row][col] == 'Q':
                return False
            row -= 1
            col -= 1
        
        row = r - 1
        col = c + 1
        while row >= 0 and col < n:
            if board[row][col] == 'Q':
                return False
            row -= 1
            col += 1
        
        return True

