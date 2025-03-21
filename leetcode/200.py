from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.claim_island(grid, i, j)
                    result += 1
        return result

    def claim_island(self, grid: List[List[str]], i: int, j: int) -> None:
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return

        if grid[i][j] == "0":
            return
        grid[i][j] = "0"
        self.claim_island(grid, i - 1, j)
        self.claim_island(grid, i + 1, j)
        self.claim_island(grid, i, j - 1)
        self.claim_island(grid, i, j + 1)


sol = Solution()
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(sol.numIslands(grid))
