class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numMap = {}

        for i in range(len(numbers)):
            numMap[numbers[i]] = i
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if (complement in numMap and numMap[complement] != i):
                return [i+1, numMap[complement] + 1]
        return []
        