class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        print(intervals)
        prevEnd = float('-inf')
        count = 0
        for start, end in intervals:
            if start < prevEnd:
                count += 1
                prevEnd = min(end, prevEnd) 
            else:
                prevEnd = end
        return count
