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
            if maxF < numCount[s[r]]:
                maxF = numCount[s[r]]

            # is this a valid window? 
            # current size - biggest char amount = chars that need swapping
            # chars that need swapping > allowed swaps
            while (r - l + 1) - maxF > k: 
                # since not valid, we need to move our left pointer
                numCount[s[l]] -= 1
                l += 1
            
            # if current valid size of window > max length that we've seen alr
            if r - l + 1 > res:
                res = r - l + 1
        return res 

        