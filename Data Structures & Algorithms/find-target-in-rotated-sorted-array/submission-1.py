class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            middle = (l + r) // 2
            if nums[middle] == target:
                return middle
            
            # are we in the left side
            if nums[middle] >= nums[l]:
                # if the target is greater than the middle 
                # or target is smaller than the leftmost value
                if target > nums[middle] or target < nums[l]:
                    l = middle + 1
                else:
                    r = middle - 1
            # we're on the right side 
            else:
                if target < nums[middle] or target > nums[r]:
                    r = middle - 1
                else:
                    l = middle + 1
        return -1 



        