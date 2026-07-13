class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()
        pairs = { 
            ")" : "(", 
            "]": "[", 
            "}" : "{" 
        }

        for c in s:
            if c in pairs:
                if stack and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        # true only if stack is empty 
        return True if not stack else False
        