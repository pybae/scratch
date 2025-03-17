from typing import Optional, Dict
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        nodes = {}
        nodes[node.val] = Node(node.val)
        queue = deque([node])
        while queue:
            current = queue.popleft()

            for neighbor in current.neighbors:
                if neighbor.val not in nodes:
                    nodes[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)
            nodes[current.val].neighbors = [nodes[neighbor.val] for neighbor in current.neighbors]

        return nodes[node.val]

#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
#         if not node:
#             return None
#         return self.cloneNode(node, {})
# 
#     def cloneNode(self, node: Optional['Node'], nodes: Dict[int, 'Node']):
#         if node.val in nodes:
#             return nodes[node.val]
#         clone = Node(node.val)
#         nodes[node.val] = clone
#         clone.neighbors = [self.cloneNode(neighbor, nodes) for neighbor in node.neighbors]
#         return clone
