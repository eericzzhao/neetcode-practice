"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sorted starting times
        start = sorted([i.start for i in intervals])
        # sorted ending times
        end = sorted([i.end for i in intervals])

        # result = max of whatever count that we've seen, counter
        res, count = 0,0
        # positioin at start and end array
        s, e = 0,0 
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res,count)
        return res

