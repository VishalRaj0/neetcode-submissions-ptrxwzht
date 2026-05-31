# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        count = 0
        dummy = head
        while dummy:
            count += 1
            dummy = dummy.next
        
        half = math.ceil(count / 2)
        dummy = head
        for i in range(half - 1):
            dummy = dummy.next
        
        temp = dummy.next
        dummy.next = prev = None
        dummy = temp
        while dummy:
            temp = dummy.next
            dummy.next = prev
            prev = dummy
            dummy = temp
        
        while prev:
            temp = head
            head = head.next
            temp.next = prev
            prev = prev.next
            temp.next.next = head




        

