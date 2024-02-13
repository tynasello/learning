# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if (not root):
            return False

        def dfs(curr, currSum):
            if (not curr.left and not curr.right):
                return True if currSum == targetSum else False

            if (curr.left):
                if (dfs(curr.left, currSum + curr.left.val)):
                    return True

            if (curr.right):
                if (dfs(curr.right, currSum + curr.right.val)):
                    return True

        return dfs(root, root.val)
