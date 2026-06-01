# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        dummy = head

        while dummy:
            count += 1
            dummy = dummy.next
        if count <= 1:
            return None
            
        target = count - n
        index = 1 
        slow = head
        fast = head.next
        if target < index:
            return fast
        while index < target:
            fast = fast.next
            slow = slow.next
            index += 1

        slow.next = fast.next
        return head