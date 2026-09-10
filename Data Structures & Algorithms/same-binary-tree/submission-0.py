# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if theyre both empty trees
        if not p and not q:
            return True
        # if anyone of the trees is null OR
        # the two root values are not the same
        if not p or not q or p.val != q.val:
            return False
        
        # this will just recursively call on both of the trees 
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))


        