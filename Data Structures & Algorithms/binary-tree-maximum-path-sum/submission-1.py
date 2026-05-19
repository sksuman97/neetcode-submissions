# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # We will do it recurssively
        ## we will maintain a global max
        ## At each node we return the max sofar to root
        ## and sum left, right, node then saves the max
        ## If the node is negative, then start the sum from zero
        self.max_path = float('-inf')
        def dfs(root):
            if root is None:
                return 0
            l_path = max(dfs(root.left),0)
            r_path = max(dfs(root.right),0)
            l_t_r = l_path+root.val+r_path ## left_to_right_path including root
            ## For extension to parent node
            # we will check the max betn left path and right path
            e_p = max(l_path, r_path, 0) ## Zero is for negative values to exclude them
            self.max_path = max(self.max_path, l_t_r)

            return e_p + root.val
        dfs(root)
        return self.max_path










        