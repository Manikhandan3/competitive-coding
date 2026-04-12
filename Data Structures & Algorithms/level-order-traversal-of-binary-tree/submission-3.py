# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(node, h) -> None:
            if not node:
                return 
            if len(res) == h:
                res.append([])
            res[h].append(node.val)
            dfs(node.left,h+1)
            dfs(node.right,h+1)
        dfs(root,0)
        return res