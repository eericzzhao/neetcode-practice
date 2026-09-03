# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # swap the children
        # save the left child and then we can make the swap between the two child nodes
        root.left, root.right = root.right, root.left

        # by calling on the function itself, it turns it recursive by calling the same function onto the children and its future grand nodes
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        