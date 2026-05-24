class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        window_s = defaultdict(int)
        matched = 0

        left = 0
        res = [-1, -1]
        min_length = float('inf')
        for right in range(len(s)):
            ch = s[right]
            window_s[ch] += 1
            if ch in count_t and count_t[ch] == window_s[ch]:
                matched += 1
            
            while matched == len(count_t):
                current_length = right - left + 1
                if current_length < min_length:
                    res = [left, right]
                    min_length = current_length 
                # shrink the window from left
                ch = s[left]
                window_s[ch] -= 1
                if ch in count_t and count_t[ch] == window_s[ch] + 1:
                    matched -= 1
                left += 1
        return s[res[0] : res[1] + 1]
                
