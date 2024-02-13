# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        self.rightViewNodes = [root.val]
        self.currLongestDepthOfStemsToRight = 1
        self.dfs(root, 1)
        return self.rightViewNodes

    def dfs(self, node, currDepth):
        if not node.right and not node.left:
            return
        if node.right:
            if currDepth + 1 > self.currLongestDepthOfStemsToRight:
                self.rightViewNodes.append(node.right.val)
                self.currLongestDepthOfStemsToRight = max(
                    self.currLongestDepthOfStemsToRight, currDepth + 1)
            self.dfs(node.right, currDepth + 1)

        if node.left:
            if currDepth + 1 > self.currLongestDepthOfStemsToRight:
                self.rightViewNodes.append(node.left.val)
                self.currLongestDepthOfStemsToRight = max(
                    self.currLongestDepthOfStemsToRight, currDepth + 1)
            self.dfs(node.left, currDepth + 1)
