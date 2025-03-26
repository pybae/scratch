from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if self.find_node(q, p):
            return q
        if self.find_node(p, q):
            return p

        node = root
        while node:
            p_in_left = node.left and self.find_node(node.left, p)
            p_in_right = node.right and self.find_node(node.right, p)
            q_in_left = node.left and self.find_node(node.left, q)
            q_in_right = node.right and self.find_node(node.right, q)

            if p_in_left and q_in_left:
                node = node.left
            elif p_in_right and q_in_right:
                node = node.right
            else:
                return node

        return node


    def find_node(self, root: TreeNode, target: TreeNode) -> bool:

        q = deque([root])
        while q:
            node = q.popleft()
            if node.val == target.val:
                return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return False


sol = Solution()


