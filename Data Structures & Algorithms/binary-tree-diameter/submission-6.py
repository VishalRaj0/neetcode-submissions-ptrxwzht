# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxdiameter = 0
        def findmaxdiameter(node):
            nonlocal maxdiameter 

            if not node:
                return 0

            countr = findmaxdiameter(node.right)
            countl = findmaxdiameter(node.left)

            diameter = countr + countl
            maxdiameter = max(maxdiameter, diameter)
            return 1 + max(countr, countl)
        
        findmaxdiameter(root)
        return maxdiameter
