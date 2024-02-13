# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        lot = []

        q = deque()
        if root:
            q.append(root)

        while q:
            nodesInCurrLevel = []
            for _ in range(len(q)):
                node = q.popleft()
                nodesInCurrLevel.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            lot.append(nodesInCurrLevel)

        return lot
