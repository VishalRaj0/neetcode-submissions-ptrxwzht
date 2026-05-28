# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = dummy = ListNode(0)

        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                dummy = dummy.next
                list1 = list1.next
            else:
                dummy.next = list2
                dummy = dummy.next
                list2 = list2.next
        
        remaining = list1 if list1 else list2
        while remaining:
            dummy.next = remaining
            dummy = dummy.next
            remaining = remaining.next

        return head.next
