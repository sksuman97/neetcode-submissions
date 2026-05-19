# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ## We will store indices using hashmap to rtrieve index in  O(n) time
        indices = {val:ind for ind, val in enumerate(inorder)}
        self.pre_ind = 0
        def dfs(l, r):
            if l>r:
                return None
            ## Get the root
            root_val = preorder[self.pre_ind]
            ## get the indices in inorder
            m = indices[root_val]
            self.pre_ind+=1 ## increase the indices for next root
            #Create root node
            root = TreeNode(root_val)
            root.left = dfs(l,m-1)
            root.right = dfs(m+1, r)
            return root
        return dfs(0, len(inorder)-1)






