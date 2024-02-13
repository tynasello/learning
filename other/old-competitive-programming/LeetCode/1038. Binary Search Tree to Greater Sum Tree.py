# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        sum = 0

        def reverseInorderTraversal(node):
            nonlocal sum
            if not node:
                return
            reverseInorderTraversal(node.right)
            sum += node.val
            node.val = sum
            reverseInorderTraversal(node.left)

        reverseInorderTraversal(root)
        return root
