class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # the the first string is bigger, then its wrong
        if len(s1) > len(s2):
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26

        # we want to get the first s1 length of characters for both
        # using array frequencies because it has a fixed size of 26
        for s in range(len(s1)):
            # we're mapping each char to their respective ascii value
            # based on the index, we're getting their count
            s1Count[ord(s1[s]) - ord('a')] += 1
            s2Count[ord(s2[s]) - ord('a')] += 1
        
        matches = 0 
        # we are going to be comparing the two arrays 
        for i in range(26):
            # if the character matches, we increment our matches
            if s1Count[i] == s2Count[i]:
                matches += 1
            
        # sliding window portion finally
        l = 0
        # with our sliding window already intitialized,
        # we can start from the length of s1
        for r in range(len(s1), len(s2)):
            # if the character counts match, then its true duh
            if matches == 26:
                return True
            
            # what character (rep. by index) is this? 
            index = ord(s2[r]) - ord('a')
            # update the count from s2Count's side
            s2Count[index] += 1
            
            # if count matches, increase our match count
            if s1Count[index] == s2Count[index]:
                matches += 1
            # if our new count actually exceeded our matches
            # this knows that they WERE equal
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            
            # when moving left pointer, we would need to remove chars
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26

