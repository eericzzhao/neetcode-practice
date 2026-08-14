class Solution:
    def findMin(self, nums: List[int]) -> int:
        # logn time --> binary search
        l, r = 0, len(nums) - 1
        minmin = 0

        while l <= r:
            m = (l + r) // 2

            if nums[m] >= nums[l]:
                l = m + 1
                minmin = min(minmin, nums[m])

            else:
                r = m - 1
                minmin = min(minmin, nums[m])

        return minmin

            

        