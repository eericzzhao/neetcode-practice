class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = r = 0
        deque = collections.deque()

        while r < len(nums):
            # valid deque and most recent appended is less than curr
            while deque and nums[deque[-1]] < nums[r]:
                deque.pop()

            # after popping the smaller valeus from q can we append
            deque.append(r)

            # remove the left pointer from the window
            if l > deque[0]:
                deque.popLeft()

            # if we're at the window length, we can start appending
            if (r + 1) >= k:
                res.append(nums[deque[0]])
                l += 1
            
            r += 1
        return res



        