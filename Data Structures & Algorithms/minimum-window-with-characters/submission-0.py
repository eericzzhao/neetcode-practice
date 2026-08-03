class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        tCount, window = {}, {}

        # get the count of the t string
        for c in t:
            tCount[c] = tCount.get(c, 0) + 1
        
        # these are counters to store what we have in our window
        # what we need in order to get a substring w/ all chars
        have, need = 0, len(tCount)
        # res wil be a [l, r] pointer, length 
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            # update the char count for our current window
            window[c] = window.get(c, 0) + 1 

            # does current window have right char +
            # the count of the char matches 
            if c in tCount and window[c] == tCount[c]:
                have += 1
            
            while have == need:
                # update our result 
                # if the current substring length > longest we've seen 
                if (r - l + 1) < resLen:
                    # our sliding window string
                    res = [l, r]
                    resLen = (r - l + 1)
                # pop fro the left of our window
                window[s[l]] -= 1
                # if the character we decremented was actually:
                # a character we need AND window < what we need 
                if s[l] in tCount and window[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1
        l, r = res 
        if resLen != float('infinity'):
            return s[l: r + 1]
        else:
            return ""


