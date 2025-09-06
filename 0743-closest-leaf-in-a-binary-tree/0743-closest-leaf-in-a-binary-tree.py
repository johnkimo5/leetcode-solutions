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
        adjList = defaultdict(list)
        q = deque([root])
        leaves = set()
        while q:
            node = q.popleft()
            if not node.left and not node.right:
                leaves.add(node.val)
            if node.left:
                adjList[node.val].append(node.left.val)
                adjList[node.left.val].append(node.val)
                q.append(node.left)
            if node.right:
                adjList[node.val].append(node.right.val)
                adjList[node.right.val].append(node.val)
                q.append(node.right)
        print(adjList)
        q = deque([k])
        visited = set([k])
        print(q)
        print(visited)
        while q:
            node = q.popleft()
            if node in leaves:
                return node
            for neighbor in adjList[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)