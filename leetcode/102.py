from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = [[]]

        q, r = deque([root]), deque()

        while q:
            node = q.popleft()
            result[-1].append(node.val)

            if node.left:
                r.append(node.left)
            if node.right:
                r.append(node.right)

            if not q and r:
                q = r
                result.append([])
                r = deque()

        return result


sol = Solution()
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(sol.levelOrder(root))
print(sol.levelOrder(TreeNode(1)))
print(sol.levelOrder(None))
