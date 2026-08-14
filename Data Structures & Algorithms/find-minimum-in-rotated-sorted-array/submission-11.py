class Solution:
    def findMin(self, nums: List[int]) -> int:
        # logn time --> binary search
        l, r = 0, len(nums) - 1
        minmin = nums[l]

        while l <= r:
            if nums[l] < nums[r]:
                minmin = min(minmin, nums[l])
                break
            m = (l + r) // 2
            minmin = min(minmin, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return minmin

            

        