class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            middl = (l + r) // 2

            # if the nubmer in our middle is greater than our target
            if nums[middl] > target:
                r = middl - 1
            # if our number is in the middle is smaller than the target
            elif nums[middl] < target:
                l = middl + 1
            else:
                return middl
        return -1 



        