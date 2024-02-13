# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.res = ''
        self.preorder_traversal(root)
        return self.res
            
        
    def preorder_traversal(self, node):
        if node is None: return
        
        self.res+=str(node.val)
        
        if(node.left or node.right):
            self.res+='('
            self.preorder_traversal(node.left)
            self.res+=')'
            
        if (node.right):
            self.res+='('
            self.preorder_traversal(node.right)
            self.res+=')'
        
        
        
        