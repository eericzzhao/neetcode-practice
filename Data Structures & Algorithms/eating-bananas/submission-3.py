import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        res = end
        while start <= end:
            k = (start + end) // 2

            timeSoFar = 0
            for p in piles:
                timeSoFar += math.ceil(p / k)
            
            if timeSoFar > h:
                start = k + 1
            else:
                res = k
                end = k - 1
        
        return res