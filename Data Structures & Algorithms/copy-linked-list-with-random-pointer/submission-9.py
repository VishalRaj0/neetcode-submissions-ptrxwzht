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
        map = {None: None}
        
        # dummy = head
        # while dummy:
        #     map[dummy] = Node(dummy.val)
        #     dummy = dummy.next

        dummy = head
        while dummy:
            if dummy.next not in map:
                map[dummy.next] = Node(dummy.next.val)

            if dummy.random not in map:
                map[dummy.random] = Node(dummy.random.val)
            
            if dummy not in map:
                map[dummy] = Node(dummy.val)

            map[dummy].next = map[dummy.next] 
            map[dummy].random = map[dummy.random] 
            

            dummy = dummy.next

        return map[head]
        