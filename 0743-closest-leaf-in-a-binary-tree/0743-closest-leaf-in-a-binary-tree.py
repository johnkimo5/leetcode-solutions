# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
find the nearest leaf node from the target k in the tree
BFS -> start from the the node, traverse edges
this requires us to create an undirected graph from the tree with edges going to the parent and children


"""
from collections import deque, defaultdict
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        parent = {}
        start = None
        def dfs(curr):
            nonlocal start
            if not curr:
                return
            if curr.val == k:
                start = curr
            if curr.left:
                parent[curr.left] = curr
            if curr.right:
                parent[curr.right] = curr
            dfs(curr.left)
            dfs(curr.right)

        dfs(root)

        q = deque([start])
        visited = set([start])
        while q:
            node = q.popleft()
            if not node.left and not node.right:
                return node.val
            for neighbor in (node.left, node.right, parent.get(node)):
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)