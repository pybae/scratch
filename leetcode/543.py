# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)[1]
    
    def dfs(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0, 0
        left_height, left_diameter = self.dfs(node.left)
        right_height, right_diameter = self.dfs(node.right)

        return max(left_height, right_height) + 1, max(left_diameter, right_diameter, left_height + right_height)
