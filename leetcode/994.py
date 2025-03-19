from typing import List, Set, Tuple

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        just_rotted = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    just_rotted.add((i, j))

        generations = 0 if just_rotted else 1
        while just_rotted:
            newly_rotted = set()
            for i, j in just_rotted:
                self.rotOrange(grid, i - 1, j, newly_rotted)
                self.rotOrange(grid, i + 1, j, newly_rotted)
                self.rotOrange(grid, i, j - 1, newly_rotted)
                self.rotOrange(grid, i, j + 1, newly_rotted)

            just_rotted = newly_rotted
            generations += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return generations - 1

    def rotOrange(self, grid: List[List[int]], i: int, j: int, newly_rotted: Set[Tuple[int, int]]):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
            grid[i][j] = 2
            newly_rotted.add((i, j))


sol = Solution()
print(sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print(sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print(sol.orangesRotting([[0,2]]))
