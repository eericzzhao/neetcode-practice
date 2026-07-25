class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 # left pointer
        longRes = 0 #output
        # store our current substring
        uniqSet = set() 

        for r in range(len(s)):
            # if we see a new repeat character
            while s[r] in uniqSet:
                # we want to now move onto a new word
                uniqSet.remove(s[l])
                # we also want to move our left pointer
                l += 1
            # otherwise if unique we just add the new char (add bc sets are unordered)
            uniqSet.add(s[r])
            # update our max substring le nght
            longRes = max(longRes, r - l + 1)
        return longRes 

        