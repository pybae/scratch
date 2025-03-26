# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if p.val > q.val:
            p, q = q, p

        current = root
        while current:
            if p.val <= current.val <= q.val:
                return current

            # current.left and current.right should always hold true if p and q exist.
            if max(p.val, q.val) < current.val:
                current = current.left
            elif min(p.val, q.val) > current.val:
                current = current.right

        return current
