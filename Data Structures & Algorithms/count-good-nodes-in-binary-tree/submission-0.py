# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxValue):
            if not node:
                return 0
            # this is a good node if the node value is greater than the maximum value that we've seen so far
            res = 1 if node.val >= maxValue else 0

            maxValue = max(node.val, maxValue)
            res += dfs(node.left, maxValue)
            res += dfs(node.right, maxValue)
            return res
        return dfs(root, root.val)
        