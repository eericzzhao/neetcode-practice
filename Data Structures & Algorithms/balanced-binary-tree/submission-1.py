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
            # this is checking for each node whether its children has a balanced tree structure
            # if we know that the left and right child nodes are balanaced (true) and that the when our parent node when we subtract it also makes a 1 or less difference in nodes.
            balanced = (left[0] and right[0] and 
                        abs(left[1] - right[1]) <= 1)
            # this is also contributing to the recursive function because this is the part that is constantly beign updated for the child nodes 
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]
        
        


