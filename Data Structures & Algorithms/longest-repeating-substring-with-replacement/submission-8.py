class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        numCount = {}
        res = 0
        maxF = 0

        for r in range(len(s)):
            numCount[s[r]] = numCount.get(s[r], 0) + 1

            if maxF < numCount[s[r]]:
                maxF = numCount[s[r]]
            while (r - l + 1) - maxF > k: 
                numCount[s[l]] -= 1
                l += 1
            if (r - l + 1) > res:
                res = r - l + 1
        return res
        