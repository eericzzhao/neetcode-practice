"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # We're sorting the start and end times
        start = sorted(i.start for i in intervals)
        end = sorted(i.end for i in intervals)

        # Storing the final room count + current room count
        result, roomCount = 0,0
        # This is to keep track of the start and end times
        s, e = 0,0

        # Iterate through the entire intervals list
        while s < len(intervals):
            # If our start time is less than our end time
            if start[s] < end[e]:
                # we can move onto the next start time to check + 1 more room
                s += 1
                roomCount += 1
            # Otherwise, if the start time we landed on was either equal or greater than the end time, then we can move on to the next meeting ending time + reduce the room count
            else:
                e += 1
                roomCount -= 1
            # Keeping consistent track of the greatest amount of rooms mean that this amount is the minimum amount of rooms that we will need during that entirety of the schedule.
            result = max(result, roomCount)
        return result
            
        