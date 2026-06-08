# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        is_same = True

        def dfs(p, q):
            nonlocal is_same

            if not is_same or (not p and not q):
                return

            if p and q and p.val == q.val:
                pass
            else:
                is_same = False
                return
            
            dfs(p.left, q.left)
            dfs(p.right, q.right)

        dfs(p, q)
        return is_same
            