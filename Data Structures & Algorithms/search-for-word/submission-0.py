class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW = len(board)
        COL = len(board[0])
        def dfs(row, col, matched_word):
            if len(matched_word) == len(word):
                return True
            
            if not (0 <= row < ROW and 0 <= col < COL):
                return False

            if board[row][col] != word[len(matched_word)]:
                return False
            matched_word += board[row][col]
            print(row, col, matched_word)
            return dfs(row + 1, col, matched_word) or dfs(row - 1, col, matched_word) or dfs(row, col + 1, matched_word) or dfs(row, col - 1, matched_word)
        
        for i in range(ROW):
            for j in range(COL):
                if dfs(i, j , ""):
                    return True
        return False