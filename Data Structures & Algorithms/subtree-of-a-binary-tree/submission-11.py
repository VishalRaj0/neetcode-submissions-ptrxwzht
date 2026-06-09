# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def check_subtree(node1, node2):
            if not node1 and not node2:
                return True
            elif node1 and node2 and node1.val == node2.val:
                print(node1.val, node2.val)
                return check_subtree(node1.left, node2.left) and check_subtree(node1.right, node2.right)
            else:
                return False
        
        def dfs(root, subroot):
            if not (root and subroot):
                return False
                
            if check_subtree(root, subroot):
                return True
            
            return dfs(root.left, subroot) or dfs(root.right, subroot)
        
        return dfs(root, subRoot)
            