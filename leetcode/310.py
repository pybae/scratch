from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # find a node without an edge, must exist, then do dfs to find length between it and every other node
        # then find max
        # actually, can't you pick any node?
        # if the lengths are equidistant already, you win, if not sum the highest two

        edge_map = {i: set() for i in range(n)}
        for a, b in edges:
            edge_map[a].add(b)
            edge_map[b].add(a)

        distances = {}
        self.dfs(0, 0, edge_map, distances)

        leaf_node = max(distances.items(), key=lambda x: x[1])[0]
        distances = {}
        self.dfs(leaf_node, 0, edge_map, distances)

        furthest_node= max(distances.items(), key=lambda x: x[1])[0]

        path = [leaf_node]
        self.find_path(leaf_node, furthest_node, path, edge_map)

        if len(path) % 2:
            return [path[len(path) // 2]]
        else:
            return [path[len(path) // 2], path[len(path) // 2 - 1]]

    def dfs(self, node: int, step: int, edge_map: dict[int, set[int]], distances: dict[int, int]):
        if node in distances:
            return distances[node]

        distances[node] = step
        for neighbor in edge_map[node]:
            self.dfs(neighbor, step + 1, edge_map, distances)

    def find_path(self, start: int, end: int, path: list[int], edge_map: dict[int, set[int]]) -> bool:
        if start == end:
            return True
        
        for neighbor in edge_map[start]:
            if neighbor in path:
                continue

            path.append(neighbor)
            if self.find_path(neighbor, end, path, edge_map):
                return True
            else:
                path.pop()

        return False


sol = Solution()
print(sol.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))
print(sol.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))
print(sol.findMinHeightTrees(3, [[0,1],[0,2]]))
