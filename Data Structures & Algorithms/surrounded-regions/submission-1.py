class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = deque()
        ROWS = len(board)
        COLS = len(board[0])

        for r in range(ROWS):
            if board[r][0] == 'O':
                q.append((r, 0))
            if board[r][COLS - 1] == 'O':
                q.append((r, COLS - 1))
        
        for c in range(COLS):
            if board[0][c] == 'O':
                q.append((0, c))
            if board[ROWS - 1][c] == 'O':
                q.append((ROWS - 1, c))
        
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
