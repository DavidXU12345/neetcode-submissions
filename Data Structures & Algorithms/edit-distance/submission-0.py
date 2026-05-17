from functools import lru_cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        @lru_cache(None)
        def dfs(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            
            res = min(dfs(i, j + 1), dfs(i + 1, j))
            res = min(res, dfs(i + 1, j + 1))
            return res + 1
        
        return dfs(0, 0)
            
