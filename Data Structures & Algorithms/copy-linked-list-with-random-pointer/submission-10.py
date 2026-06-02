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
        map = defaultdict(lambda: Node(0))
        map[None] = None
        
        dummy = head
        while dummy:
            map[dummy].val = dummy.val 
            map[dummy].next = map[dummy.next]
            map[dummy].random = map[dummy.random] 
            dummy = dummy.next

        return map[head]
        