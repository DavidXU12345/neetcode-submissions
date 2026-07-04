from functools import lru_cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        @lru_cache(None)
        def dfs(i, j):
            k = i + j
            if k == len(s3):
                return (i == len(s1)) and (j == len(s2))

            res = False
            if i < len(s1) and s3[k] == s1[i]:
                res |= dfs(i + 1, j)
            
            if j < len(s2) and s3[k] == s2[j]:
                res |= dfs(i, j + 1)
            
            return res
        
        return dfs(0, 0)