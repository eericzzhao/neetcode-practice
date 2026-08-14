class Solution:
    def findMin(self, nums: List[int]) -> int:
        # logn time --> binary search
        l, r = 0, len(nums) - 1
        minmin = float('inf')

        while l <= r:
            m = (l + r) // 2

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
            minmin = min(minmin, nums[m])
        return minmin

            

        