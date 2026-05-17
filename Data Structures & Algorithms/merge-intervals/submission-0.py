class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for i, interval in enumerate(intervals):
            if res and res[-1][1] >= interval[0]:
                res[-1][0] = min(res[-1][0], interval[0])
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(intervals[i])
        return res