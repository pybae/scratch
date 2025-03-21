from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "[]"

        l, q = [], deque([root])
        while q:
            node = q.popleft()
            if node:
                l.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                l.append("None")

        # Optional: trim trailing "None"s for cleaner output
        while l and l[-1] == "None":
            l.pop()

        return "[" + ", ".join(l) + "]"

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data or data == "[]":
            return None

        values = data.strip("[]").split(",")
        values = [v.strip() for v in values]

        root = TreeNode(int(values[0]))
        q = deque([root])
        i = 1

        while q and i < len(values):
            node = q.popleft()

            # Left child
            if i < len(values) and values[i] != "None":
                node.left = TreeNode(int(values[i]))
                q.append(node.left)
            i += 1

            # Right child
            if i < len(values) and values[i] != "None":
                node.right = TreeNode(int(values[i]))
                q.append(node.right)
            i += 1

        return root
