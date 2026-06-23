# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.res = ""
        def dfs(node):
            if not node:
                self.res += "N,"
                return None

            self.res += f"{node.val},"
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.res[:-1]
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(',')
        self.i = -1
        def dfs():
            self.i += 1
            if data[self.i] == 'N':
                return None
            
            return TreeNode(
                data[self.i],
                dfs(),
                dfs()
            )
        
        self.res = dfs()
        return self.res

