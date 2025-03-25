import math

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.is_valid_node(root, -math.inf, math.inf)

    def is_valid_node(self, node: Optional[TreeNode], _min: int, _max: int) -> bool:
        if not node:
            return True

        if node.val <= _min or node.val >= _max:
            return False

        return (self.is_valid_node(node.left, _min, node.val) and 
                self.is_valid_node(node.right, node.val, _max))


sol = Solution()
root = TreeNode(2, TreeNode(1), TreeNode(3))
print(sol.isValidBST(root))

root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
print(sol.isValidBST(root))
