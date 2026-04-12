"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def same(g) -> bool:
            val = g[0][0]
            for i in range(len(g)):
                for j in range(len(g)):
                    if val != g[i][j]:
                        return False
            return True

        if same(grid):
            root = Node(grid[0][0],True,None,None,None,None)
        else:
            root = Node(1,False,None,None,None,None)
            n = len(grid)//2
            root.topLeft = self.construct([row[:n] for row in grid[:n]])
            root.topRight = self.construct([row[n:] for row in grid[:n]])
            root.bottomLeft = self.construct([row[:n] for row in grid[n:]])
            root.bottomRight = self.construct([row[n:] for row in grid[n:]])
        return root
