class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW = len(board)
        COL = len(board[0])
        visited = set()
        def dfs(row, col, i):
            if i == len(word):
                return True
            
            if not (0 <= row < ROW and 0 <= col < COL):
                return False

            if (row, col) in visited or board[row][col] != word[i]:
                return False
            visited.add((row, col))

            i += 1
            res = (dfs(row + 1, col, i) 
            or dfs(row - 1, col, i) 
            or dfs(row, col + 1, i) 
            or dfs(row, col - 1, i))
            visited.remove((row, col))
            return res
        
        for r in range(ROW):
            for c in range(COL):
                if dfs(r, c, 0):
                    return True
        return False