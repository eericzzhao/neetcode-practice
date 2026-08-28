class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tort, hare = 0, 0 
        while True:
            # val of the slow, fast pointers
            tort = nums[tort]
            hare = nums[nums[hare]]

            if tort == hare:
                break
        
        tort2 = 0
        while True:
            tort = nums[tort]
            tort2 = nums[tort2]
            if tort == tort2:
                return tort
        