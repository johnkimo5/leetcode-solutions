# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # split or don't split
        if not root:
            return 0
        self.maxPathSum = root.val
        def helper(curr):
            if not curr:
                return 0
            left = helper(curr.left)
            right = helper(curr.right)
            left = max(left, 0)
            right = max(right, 0)
            self.maxPathSum = max(self.maxPathSum, left + right + curr.val)
            return curr.val + max(left, right)
        helper(root)
        return self.maxPathSum