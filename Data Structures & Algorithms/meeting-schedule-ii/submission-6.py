"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted(interval.start for interval in intervals)
        end = sorted(interval.end for interval in intervals)

        s = e = 0
        res = current_count = 0
        while s < len(intervals):
            # a new meeting is satrted before any of current meetings end, need a new room
            if start[s] < end[e]:
                s += 1
                current_count += 1
            else:  # a meeting is ended, free a room
                e += 1
                current_count -= 1
            res = max(res, current_count)
        return res