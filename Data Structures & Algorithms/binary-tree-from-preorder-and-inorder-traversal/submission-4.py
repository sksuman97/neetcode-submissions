# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val:ind for ind, val in enumerate(inorder)}
        self.pre_ind = 0
        ## l and r are index for 
        def dfs(l, r):
            if l>r:
                return None
            ## Find the root node
            root_val = preorder[self.pre_ind]
            self.pre_ind+=1
            root = TreeNode(root_val)
            ## Find the index of root in inorder
            m = indices[root_val]
        
            ## Assign left side and right side
            root.left = dfs(l, m-1)
            root.right = dfs(m+1, r)
            return root
        return dfs(0, len(inorder)-1)








