# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0

        dummy = head
        while dummy:
            length += 1
            dummy = dummy.next
        
        dummy = head
        res = ListNode(0)
        segment = res
        for i in range(length // k):
            prev = None
            segment_end = None
            for j in range(k):
                if j == 0:
                    segment_end = dummy
                temp = dummy.next
                dummy.next = prev
                prev = dummy
                dummy = temp
            segment.next = prev
            segment = segment_end
        
        if dummy:
            segment.next = dummy
        
        return res.next