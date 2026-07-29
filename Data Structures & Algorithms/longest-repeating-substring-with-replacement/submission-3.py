class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        numCount = {}
        res = 0

        maxF = 0

        # right pointer 
        for r in range(len(s)):
            # updating the count of the character
            numCount[s[r]] = numCount.get(s[r], 0) + 1
            # constant operation: we're just constantly checking: Is this the new greatest amount of a character
            maxF = max(maxF, numCount[s[r]])

            # is this a valid window? 
            # current size - biggest char amount = chars that need swapping
            # chars that need swapping > allowed swaps
            while (r - l + 1) - maxF > k: 
                # since not valid, we need to move our left pointer
                numCount[s[l]] -= 1
                l += 1
            
            # size of window 
            res = max(res, r - l + 1)
            r += 1
        return res 

        