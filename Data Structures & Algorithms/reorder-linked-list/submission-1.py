# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
         # what we're doing here is moving our node pointers to the halfway point, by setting up our faster node to be instead to the next of it and then moving by 2, it'll reach the end by the time the slower node reaches the halfway point 
        tort, hare = head, head.next
        while hare and hare.next:
            tort = tort.next
            hare = hare.next.next

        # next we need to flip the order of the second half 
        second = tort.next # this is the start of the second half 
        # our slow next is our last node -> Null, 
        prev = tort.next = None 

        while second:
            # 
            temp = second.next
            second.next = prev
            prev = second 
            second = temp 
        
        # now that its been reversed - we need to merge them
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second 
            second.next = temp1 
            first,second = temp1, temp2 

        