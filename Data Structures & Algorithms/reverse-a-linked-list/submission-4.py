# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        # iterative approach
        while curr:
            # we need a temp varaible to store next value
            nxt = curr.next
            # we move the prev value to the front 
            curr.next = prev
            # our current value becomes our previous one
            prev = curr
            # since we replaced the next value, we take the temp value and moved our current to be that now
            curr = nxt
        return prev