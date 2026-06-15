# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def traverse(node, biggest):
            nonlocal res
            if not node:
                return None

            print(node.val, biggest)
            if node.val >= biggest:
                res += 1
                biggest = node.val
            
            traverse(node.left, biggest)
            traverse(node.right, biggest)
        
        traverse(root, float('-inf'))
        return res