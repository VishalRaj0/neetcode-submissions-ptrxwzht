# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode(0)
        dummy = res

        while True:
            lowest = ListNode(float('inf'))
            lowest_index = None
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if lists[i].val <= lowest.val:
                    lowest = lists[i]
                    lowest_index = i

            if lowest_index == None:
                break
            lists[lowest_index] = lists[lowest_index].next
            lowest.next = None
            dummy.next = lowest
            dummy = dummy.next
        
        return res.next
            
                