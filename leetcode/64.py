from typing import List
import math

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        cache = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        return self.dfs(grid, 0, 0, cache)

    def dfs(self, grid, i, j, cache) -> int:
        if i >= len(grid) or j >= len(grid[0]):
            return math.inf

        if cache[i][j] != 0:
            return cache[i][j]

        ans = 0
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            ans = grid[i][j]
        else:
            ans = grid[i][j] + min(self.dfs(grid, i, j + 1, cache),
                                   self.dfs(grid, i + 1, j, cache))

        cache[i][j] = ans
        return ans

sol = Solution()
print(sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
print(sol.minPathSum([[1, 2, 3], [4, 5, 6]]))
