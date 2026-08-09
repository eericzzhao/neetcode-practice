class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        result = r

        while l <= r:
            mid = (l + r) // 2
            hours = 0

            for p in piles:
                hours += math.ceil(p / mid)
            # rememeber we dont want this if statement inside because we want to calcualte the hours foe the entire list 
            if hours <= h:
                result = min(result, mid)
                    # this means that we've been eating more bananas per hour than we need to, we can find a smaller amount of bananas 
                r = mid - 1
            else:
                    # this means that we've beem eating too little bananas at each hour to reach the time 
                l = mid + 1
        return result
        
        