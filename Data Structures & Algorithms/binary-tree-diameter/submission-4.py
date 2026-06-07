# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxdiameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def findmaxdiameter(node):
            if not node:
                return 0

            countr = findmaxdiameter(node.right)
            countl = findmaxdiameter(node.left)

            diameter = countr + countl
            self.maxdiameter = max(self.maxdiameter, diameter)
            return 1 + max(countr, countl)
        
        findmaxdiameter(root)
        return self.maxdiameter
