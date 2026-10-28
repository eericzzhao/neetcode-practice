class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        arr = []
        for val, cnt in freq.items():
            arr.append([cnt, val])
        arr.sort()

        temp = []
        while len(temp) < k:
            temp.append(arr.pop()[1])
        return temp
        