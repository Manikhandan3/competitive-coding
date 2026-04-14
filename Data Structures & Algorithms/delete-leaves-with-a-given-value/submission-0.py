# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node) -> bool:
            if not node:
                return True
            
            l = dfs(node.left)
            r = dfs(node.right)
            if l: node.left = None
            if r: node.right = None
            if l and r and node.val == target:
                return True
            else:
                return False
        
        return root if not dfs(root) else None
