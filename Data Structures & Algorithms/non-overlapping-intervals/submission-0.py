class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        lastInterval = None
        count = 0
        for i, interval in enumerate(intervals):
            if lastInterval and interval[0] < lastInterval[1]:
                count += 1
            else:
                lastInterval = interval
        return count
