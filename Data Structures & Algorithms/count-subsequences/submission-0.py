from functools import lru_cache

class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        @lru_cache(None)
        def dfs(i, j):
            if j == len(t):
                return 1
            
            if i == len(s):
                return 0
            count = 0
            if s[i] == t[j]:
                count += dfs(i + 1, j + 1)
            
            count += dfs(i + 1, j)
            return count
        
        return dfs(0, 0)
