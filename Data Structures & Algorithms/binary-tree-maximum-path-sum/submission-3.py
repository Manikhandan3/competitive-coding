# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def dfs(node) -> int:
            nonlocal res
            if not node:
                return 0
            
            l = dfs(node.left)
            if l < 0:
                l = 0
            r = dfs(node.right)
            if r < 0:
                r = 0
            res = max(res,l + r + node.val)
            return max(node.val+l,node.val+r)
        dfs(root)
        return res
