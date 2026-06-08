# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        is_balanced = True
        def dfs(node):
            nonlocal is_balanced
            
            if not is_balanced or not node:
                return 0

            countl = dfs(node.left)
            countr = dfs(node.right)
            
            if abs(countl - countr) > 1:
                is_balanced = False
                return 0
            
            return 1 + max(countl, countr)
        
        dfs(root)
        return is_balanced 