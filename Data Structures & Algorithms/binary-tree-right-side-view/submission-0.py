# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = collections.deque([root])

        res = []

        while queue:
            weAreRight = None

            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    weAreRight = node
                    queue.append(node.left)
                    queue.append(node.right)
            if weAreRight:
                res.append(weAreRight.val)
        return res

        