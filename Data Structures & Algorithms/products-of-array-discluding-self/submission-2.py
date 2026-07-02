class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        # we make the result array to be the same size as the nums list
        res = [1] * nums_len 
        prefix = 1 # temp value to remember the previous value
        for i in range(nums_len):
            res[i] = prefix # sets the first number to be the prefix number
            prefix *= nums[i] # sets our temp value to be the product of the current nums value
        postfix = 1 # we start with 1 because we want to skip the first value
        # go backwards now [range(start, stop, step])
        for i in range(nums_len - 1, -1, -1):
            # we can sart multiplying the current number and update res
            res[i] *= postfix
            # update our postfix to be whatever we see in nums now
            postfix *= nums[i]
        return res

