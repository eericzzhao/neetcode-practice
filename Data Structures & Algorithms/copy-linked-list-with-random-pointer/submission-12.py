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
        remap = { None: None }
        
        curr = head
        while curr:
            copy = Node(curr.val)
            remap[curr] = copy
            curr = curr.next
        # the point of the hash map is to create pointer connections to each respective node 
        curr = head
        while curr:
            copy = remap[curr]
            copy.next = remap[curr.next]
            copy.random = remap[curr.random]
            curr = curr.next
        return remap[head]
        