class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        res = ""

        l = 0
        window = defaultdict(int)
        matched_chars = set()
        for r in range(len(s)):
            if s[r] in t_count:
                window[s[r]] += 1
                if window[s[r]] >= t_count[s[r]]:
                    matched_chars.add(s[r])
                while len(matched_chars) == len(t_count):
                    if not res or len(res) > r - l + 1:
                        res = s[l : r + 1]
                    if s[l] in t_count:
                        window[s[l]] -= 1
                        if window[s[l]] < t_count[s[l]]:
                            matched_chars.remove(s[l])
                    l += 1
        return res
