# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val if root else 0

        def dfs(node):
            if not node:
                return 0

            leftsum = max(0, dfs(node.left))
            rightsum = max(0, dfs(node.right))
            
            cursum = leftsum + rightsum + node.val
            self.res = max(self.res, cursum)
            return node.val + max(leftsum, rightsum)
        
        dfs(root)
        return self.res