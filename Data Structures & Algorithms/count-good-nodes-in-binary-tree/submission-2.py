# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def goodNodes(self, root: TreeNode) -> int:
#         max_ = float('-inf')
#         count = 0
#         def dfs(node,max_):
#             nonlocal count
#             if not node:
#                 return
#             if node.val>=max_:
#                 count+=1
#             max_ = max(max_, node.val)
#             dfs(node.left, max_)
#             dfs(node.right, max_)
        
#         dfs(root, max_)
#         return count
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        from collections import deque
        if not root:
            return 0
        count = 0
        max_ = float('-inf')
        queue = deque([(root, max_)]) ## node and depth
        while queue:
            node, max_ = queue.popleft()
            if node.val>=max_:
                count+=1

            # keeping max for child nodes
            max_ = max(max_, node.val)
            if node.left:
                queue.append((node.left, max_))
            if node.right:
                queue.append((node.right, max_))
        
        return count

        

















        