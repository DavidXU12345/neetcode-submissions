class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_to_latest_idx: Dict[str, int] = {}
        l = 0
        res = 0

        for r, ch in enumerate(s):
            if ch in char_to_latest_idx:
                l = max(char_to_latest_idx[ch] + 1, l)
            char_to_latest_idx[ch] = r
            res = max(res, r - l + 1)
        return res




