from functools import lru_cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @lru_cache(None)
        def dfs(i, j, k):
            if k == len(s3):
                return True
            res = False
            if i < len(s1) and s1[i] == s3[k]:
                res = res or dfs(i + 1, j, k + 1)
            if j < len(s2) and s2[j] == s3[k]:
                res = res or dfs(i, j + 1, k + 1)
            return res
        
        if len(s1) + len(s2) != len(s3):
            return False
        
        return dfs(0, 0, 0)