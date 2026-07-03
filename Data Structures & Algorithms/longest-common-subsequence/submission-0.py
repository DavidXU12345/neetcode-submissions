from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(None)
        def helper(i, j, current_length):
            if i == len(text1) or j == len(text2):
                return current_length
            
            length = max(helper(i, j + 1, current_length),  helper(i + 1, j, current_length))
            if text1[i] == text2[j]:
                length = max(length, helper(i + 1, j + 1, current_length + 1))

            return length
           
        
        return helper(0, 0, 0)