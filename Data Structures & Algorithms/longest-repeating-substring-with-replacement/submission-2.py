class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        res = 0

        left = 0
        max_frequency = 0

        for right in range(len(s)):
            count[s[right]] += 1
            max_frequency = max(max_frequency, count[s[right]])
            """
            max_frequency only ever needs to increase to find a longer window than the current best. 
            If it were to decrease, the window would shrink
            but we already know a window of that smaller size is achievable, so it's pointless to track.
            """
            while right - left + 1 - max_frequency > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res