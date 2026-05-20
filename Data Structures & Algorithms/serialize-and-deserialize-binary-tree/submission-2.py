# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def preorder(root):
            if root is None:
                res.append('N')
                return None
            res.append(str(root.val)) ## storing the root
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ','.join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        ## Retrieving from preorder
        vals = data.split(',')
        self.i= 0
        def retrieve():
            root_val = vals[self.i]
            if root_val=='N':
                self.i+=1
                return None
            root = TreeNode(root_val)
            self.i+=1
            root.left = retrieve()
            root.right = retrieve()
            return root
        return retrieve()





