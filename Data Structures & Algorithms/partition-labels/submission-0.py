class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = dict()
        for i, ch in enumerate(s):
            lastIdx[ch] = i
        # print(lastIdx)
        res = []
        l = r = 0
        while l < len(s):
            r = lastIdx[s[l]]
            for i in range(l, r):
                r = max(r, lastIdx[s[i]])
            res.append(r - l + 1)
            l = r + 1
        
        return res
            