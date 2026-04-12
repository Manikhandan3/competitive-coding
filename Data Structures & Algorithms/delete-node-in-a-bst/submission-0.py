# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def replace(root,node) -> Optional[TreeNode]:
            if not root and not node:
                return None
            if not root:
                return node
            if not node:
                return root
            root.right = replace(root.right, node)
            return root

        if not root:
            return None
        if root.val == key:
            return replace(root.left,root.right)
        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        else:
            root.right = self.deleteNode(root.right,key)
        return root