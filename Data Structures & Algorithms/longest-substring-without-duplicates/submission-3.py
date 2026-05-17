class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        char_to_latest_idx: Dict[str, int] = {}
        res = 0

        for r, ch in enumerate(s):
            if ch in char_to_latest_idx:
                l = char_to_latest_idx[ch] + 1
            char_to_latest_idx[ch] = r
            res = max(res, r - l + 1)
        return res




