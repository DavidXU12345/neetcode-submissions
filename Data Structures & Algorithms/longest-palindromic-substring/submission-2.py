class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1
        
        res = ''
        for i in range(len(s)):
            left, right = helper(i, i)
            if right - left + 1 > len(res):
                res = s[left : right + 1]
            
            left, right = helper(i, i + 1)
            if right - left + 1 > len(res):
                res = s[left : right + 1]
        
        return res
