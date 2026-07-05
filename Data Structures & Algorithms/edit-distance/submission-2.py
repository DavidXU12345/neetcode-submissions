from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        @cache
        def dfs(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            res = float('inf')
            # insert
            res = min(res, 1 + dfs(i, j + 1))

            # delete
            res = min(res, 1 + dfs(i + 1, j))

            # replace
            res = min(res, 1 + dfs(i + 1, j + 1))

            return res
        
        return dfs(0, 0)