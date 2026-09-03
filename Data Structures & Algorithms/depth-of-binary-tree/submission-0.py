# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # dfs
        # so with this, we're retaining the depth size at each node and just continoously adding 
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        # bfs 
        # so with this strategy, we're appending all of the nodes until we reach a point where we cant anymore, 
        level = 0
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            level += 1
        return level
        
        # iterative DFS
        # stack = [[root, 1]]
        # res = 0
        # while stack: 
        #     node, depth = stack.pop()

        #     if node:
        #         res = max(res, depth)
        #         stack.extend([node.left, depth + 1])
        #         stack.extend([node.right, depth + 1])
        # return res

