class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda firstVal: firstVal[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            lastVal = res[-1][1]
            
            if start <= lastVal:
                res[-1][1] = max(lastVal, end)
            else:
                res.append([start, end])
            
        return res
        