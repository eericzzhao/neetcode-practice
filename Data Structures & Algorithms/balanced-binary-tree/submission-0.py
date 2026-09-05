# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # this will return the an array with a [boolean of whether its balanced or not, height of the tree]
        def dfs(node):
            if not node:
                return [True, 0]

            # this is the recurisve function that will keep repeating until we get to the very bottom of the left and right nodes
            left, right = dfs(node.left), dfs(node.right)
            balance = abs(left[1] - right[1])


