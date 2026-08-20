# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # avoids the worries of inserting in to an empty list 
        temp = ListNode()
        tail = temp

        # we keep going «while both of the lists are still valid 
        while list1 and list2:
            # if our second list's value is greater than the firs tone
            if list1.val < list2.val:
                # our result list next va;lue should be the smallest one and then we update our next node 
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            # we need to now move the pointer for the result list
            tail = tail.next 

        # what if one of them has reached the end
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return temp.next



        