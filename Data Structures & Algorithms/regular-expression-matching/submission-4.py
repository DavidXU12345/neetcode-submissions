from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dfs(i, j):
            if i == len(s):
                # remaining pattern must be all x* pairs
                while j + 1 < len(p) and p[j + 1] == '*':
                    j += 2
                return j == len(p)
            
            if j == len(p):
                return i == len(s)
            
            match = s[i] == p[j] or p[j] == '.'
            if (j + 1) < len(p) and p[j + 1] == '*':
                return dfs(i, j + 2) or (match and dfs(i + 1, j))   
            if match:
                return dfs(i + 1, j + 1)
            
            return False
        return dfs(0, 0)