class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW = len(board)
        COL = len(board[0])
        def dfs(row, col, matched_word, visited):
            if len(matched_word) == len(word):
                return True
            
            if not (0 <= row < ROW and 0 <= col < COL):
                return False

            if (row, col) in visited:
                return False
            
            if board[row][col] != word[len(matched_word)]:
                return False
            matched_word += board[row][col]
            visited.add((row, col))

            res = (dfs(row + 1, col, matched_word, visited) 
            or dfs(row - 1, col, matched_word, visited) 
            or dfs(row, col + 1, matched_word, visited) 
            or dfs(row, col - 1, matched_word, visited))

            visited.remove((row, col))
            return res
        
        for i in range(ROW):
            for j in range(COL):
                visited = set()
                if dfs(i, j , "", visited):
                    return True
        return False