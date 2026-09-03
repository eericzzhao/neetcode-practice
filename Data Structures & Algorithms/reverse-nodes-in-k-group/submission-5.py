# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevNode = dummy

        while True:
            kthNode = self.getKthNode(prevNode, k)
            # if we reach outside of the linked list then its a case that we can break out of. 
            if not kthNode:
                break
            nextGroup = kthNode.next 

            # we have this setup where our prev starts at the new group because we want to set the this gorups last node to be pointing there and the current node to be the group's start 
            prev, curr = kthNode.next, prevNode.next
            # reversal process where the end is set to the node before
            while curr != nextGroup:
                temp = curr.next 
                curr.next = prev
                prev = curr
                curr = temp 
            
            groupTail = prevNode.next
            prevNode.next = prev
            prevNode = groupTail
        return dummy.next 
    
    def getKthNode(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1
        return node
        