class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(row, col, matched):
            # print(matched)
            if board[row][col] != word[matched]:
                return False
            matched += 1

            if matched == len(word):
                return True
            
            seen.add((row, col))
            for d in directions:
                new_row = row + d[0]
                new_col = col + d[1]
                if 0 <= new_row < ROWS and 0 <= new_col < COLS and (new_row, new_col) not in seen:
                    if dfs(new_row, new_col, matched):
                        return True
            seen.remove((row, col))
            return False

        for r in range(ROWS):
            for c in range(COLS):
                seen = set()
                if dfs(r, c, 0):
                    return True
        return False
