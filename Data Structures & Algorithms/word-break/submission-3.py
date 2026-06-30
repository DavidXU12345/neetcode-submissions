from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        @lru_cache(None)
        def dfs(i):
            if i == len(s):
                return True

            for j in range(i, len(s)):
                if s[i : j + 1] in word_set:
                    if dfs(j + 1):
                        return True
            
            return False
        
        return dfs(0)