class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        tCount, sCount = {}, {}
        for c in t:
            tCount[c] = tCount.get(c, 0) + 1
        
        have, need = 0, len(tCount)
        res, resLen = [-1, -1], float('infinity')

        l = 0
        for r in range(len(s)):
            # setup for the right pointer char
            c = s[r]
            # update char on our window
            sCount[c] = sCount.get(c, 0) + 1

            # check if the character that we're looking is alr contained alr and if the count is matching
            if c in tCount and sCount[c] == tCount[c]:
                have += 1
            # when we re
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                
                sCount[s[l]] -= 1
                if s[l] in tCount and sCount[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        if resLen != float('infinity'):
            return s[l:r + 1]
        else:
            return ""


        