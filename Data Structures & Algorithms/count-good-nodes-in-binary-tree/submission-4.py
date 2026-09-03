# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node,val):
            nonlocal res

            if not node:
                return 
            
            if node.val >= val:
                res += 1

            dfs(node.left,max(val,node.val))
            dfs(node.right,max(val,node.val))
        
        dfs(root,float('-inf'))
        return res