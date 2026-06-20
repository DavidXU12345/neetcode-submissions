class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = -1
        prev_end = float('inf')
        for i in range(len(intervals)):
            if intervals[i][0] < prev_end:
                prev_end = min(intervals[i][1], prev_end)
                # print(prev_end)
                res += 1
            else:
                prev_end = intervals[i][1]
        return 0 if res == -1 else res