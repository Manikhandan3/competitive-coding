# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node) -> List[int]:
            # nonlocal res
            if not node:
                return [0,0]
            
            l = dfs(node.left)
            r = dfs(node.right)
            node.val = max(l[0]+r[0], node.val+l[1]+r[1])
            return [node.val,l[0]+r[0]]
        res = dfs(root)
        return max(res[0],res[1])
        