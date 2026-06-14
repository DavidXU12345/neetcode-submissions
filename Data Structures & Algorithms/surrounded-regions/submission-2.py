class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = deque()
        ROWS = len(board)
        COLS = len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS - 1 or
                    c == 0 or c == COLS - 1) and board[r][c] == "O":
                    q.append((r, c))
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                board[r][c] = '#'
                for dr, dc in directions:
                    new_row, new_col = r + dr, c + dc
                    if (0 <= new_row < ROWS and 0 <= new_col < COLS and board[new_row][new_col] == 'O'):
                        q.append((new_row, new_col))
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'
