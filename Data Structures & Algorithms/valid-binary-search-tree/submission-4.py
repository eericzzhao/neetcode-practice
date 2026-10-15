# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, leftBound, rightBound):
            # if we reach a non-node, we still want to continue because we havent broken any of the BST rules
            if not node:
                return True
            
            # if we reach a point where we break this required rule about binary search trees, we know FOR SURE this true is invalid
            if not (node.val > leftBound and node.val < rightBound):
                return False
            
            # we want to recursively call this for the rest of our nodes in respect to the rules for the left side and the right side
            return (valid(node.left, leftBound, node.val) and
                    valid (node.right, node.val, rightBound))
        
        # we use infinity as it will be impossible to be less than or greater than these default respective infinity valuyes
        return valid(root, float('-inf'), float('inf'))
        