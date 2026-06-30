from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        @lru_cache(None)
        def dfs(left, right):
            # print(left, right)
            if left == len(s):
                return True
            if right == len(s):
                return False
            res = False
            if s[left:right + 1] in word_set:
                res |= dfs(right + 1, right + 1)
            res |= dfs(left, right + 1)
            return res
        
        return dfs(0, 0)