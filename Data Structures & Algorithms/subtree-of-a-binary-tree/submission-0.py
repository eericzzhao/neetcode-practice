# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base case
        # if the subroot is empty, then its a valid subtree
        if not subRoot:
            return True
        # if the main tree is empty and the subtree is a non-empty, then there does not exist a valid subtree
        if not root:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))



    def sameTree(self, s, t):
        # if both empty, then its a valid subtree
        if not s and not t:
            return True
        
        # if oth are non-empty 
        if s and t and s.val == t.val:
            return (self.sameTree(s.left, t.left) and
                    self.sameTree(s.right, t.right))
        # if one of them is empty, then its False
        return False
        