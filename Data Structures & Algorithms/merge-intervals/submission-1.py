class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sortig the entire input and iterating O(nlogn)
        # sort the intervals by the first value in each interval 
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        # we go over each of the first and last value in each interval
        for start, end in intervals[1:]:
            # end value of the most recent interval
            lastEnd = output[-1][1]

            # if the new interval that we see starts off smaller or equal to the last appended interval that we saw 
            if start <= lastEnd:
                # if the next one starts off smaller, then we can update the last appended interval's end to whichever is greater: the new interval's end or the one that we already saw before
                output[-1][1] = max(lastEnd, end)

            # this just means that the new interval that we saw is greater than the end of the most recently appended interval and we canm just append it as it is
            else:
                output.append([start, end])
            # [1,5], [2, 4]
        return output

        