class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        seen = set()
        res = 1
        while j < len(s):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            res = max(res, j - i + 1)
            seen.add(s[j])
            j += 1
        return res
