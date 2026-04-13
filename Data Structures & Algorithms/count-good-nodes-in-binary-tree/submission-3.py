# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node,n) -> None:
            nonlocal res

            if not node:
                return 
            if node.val >= n:
                res += 1
                n = node.val
            dfs(node.left,n)
            dfs(node.right,n)
        
        dfs(root,root.val)
        return res


            
            
            
