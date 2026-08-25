"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Map each original node to its copied node
        copyMap = {}
        curr = head

        # First pass: create copies
        while curr:
            copyMap[curr] = Node(curr.val)
            curr = curr.next

        # Second pass: connect next and random pointers
        for real, copy in copyMap.items():
            if real.next:
                copy.next = copyMap[real.next]
            if real.random:
                copy.random = copyMap[real.random]

        return copyMap[head]