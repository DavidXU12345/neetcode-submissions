class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = dict()
        for i, ch in enumerate(s):
            last_idx[ch] = i
        
        size = end = 0
        res = []
        for i, ch in enumerate(s):
            end = max(end, last_idx[ch])
            size += 1
            if i == end:
                res.append(size)
                size = 0
        
        return res