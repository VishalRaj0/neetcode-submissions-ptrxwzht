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
        if not head:
            return None
        map = {}
        
        dummy = head
        while dummy:
            map[dummy] = Node(dummy.val)
            dummy = dummy.next

        dummy = head
        while dummy:
            map[dummy].next = map[dummy.next] if dummy.next else None
            map[dummy].random = map[dummy.random] if dummy.random else None

            dummy = dummy.next

        return map[head]
        