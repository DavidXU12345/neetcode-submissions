class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        counts = [0] * 26

        res = 0
        for r in range(len(s)):
            counts[ord(s[r]) - ord('A')] += 1
            if r - l + 1 - max(counts) <= k:
                res = max(res, r - l + 1)
            else:
                counts[ord(s[l]) - ord('A')] -= 1
                l += 1
        
        return res
        