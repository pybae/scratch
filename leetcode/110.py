# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.calculateDepth(root) != -1


    def calculateDepth(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        left_depth = self.calculateDepth(node.left)
        right_depth = self.calculateDepth(node.right)

        if left_depth == -1 or right_depth == -1:
            return -1
        if abs(left_depth - right_depth) > 1:
            return -1
        return max(left_depth, right_depth) + 1
