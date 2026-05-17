"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [interval.start for interval in intervals]
        end = [interval.end for interval in intervals]
        start.sort()
        end.sort()
        startIdx = endIdx = 0
        count = res = 0
        while startIdx < len(start):
            if start[startIdx] < end[endIdx]:
                startIdx += 1
                count += 1
            else:
                endIdx += 1
                count -= 1
            res = max(res, count)
        return count
