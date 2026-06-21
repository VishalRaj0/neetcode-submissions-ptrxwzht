# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = []
        def dfs(node):
            nonlocal inorder
            if not node or len(inorder) >= k:
                return 

            dfs(node.left)
            inorder.append(node.val)
            dfs(node.right)
        
        dfs(root)
        print(inorder)
        return inorder[k - 1]
            