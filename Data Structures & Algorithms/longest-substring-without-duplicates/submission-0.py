class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longRes = 0
        uniqSet = set()

        for r in range(len(s)):
            while s[r] in uniqSet:
                uniqSet.remove(s[l])
                l += 1
            uniqSet.add(s[r])
            longRes = max(longRes, r - l + 1)
        return longRes
            
        