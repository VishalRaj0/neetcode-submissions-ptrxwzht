# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        isValid = True

        def dfs(node, interval):
            nonlocal isValid
            if not node or not isValid:
                return None

            if interval[0] < node.val < interval[-1]:
                dfs(node.left, [interval[0], node.val])
                dfs(node.right, [node.val, interval[-1]])
            else:
                isValid = False
                return
            

        dfs(root, interval=[float('-inf'), float('inf')])
        return isValid
