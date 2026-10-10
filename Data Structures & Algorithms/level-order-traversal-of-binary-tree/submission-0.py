# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # this will store our upcoming children to append
        queue = collections.deque()
        # this will basically start our loop 
        queue.append(root)

        res = []
        while queue:
            # level will store the list of values in their level
            levelVals = []
            for i in range(len(queue)):
                # we will basically keep popping all of the nodes at this level 
                node = queue.popleft()
                if node:
                    # first we append the value at this node 
                    levelVals.append(node.val)
          
                    # then we get both of the child nodses
                    queue.append(node.left)
                    queue.append(node.right)
            if levelVals:
                res.append(levelVals)
        return res



        