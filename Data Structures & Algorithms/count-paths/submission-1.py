from functools import lru_cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(None)
        def dfs(r, c):
            if not (0 <= r < m and 0 <= c < n):
                return 0
            if r == m - 1 and c == n - 1:
                return 1
            
            return dfs(r + 1, c) + dfs(r, c + 1)
        
        return dfs(0, 0)