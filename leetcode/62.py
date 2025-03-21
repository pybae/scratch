import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, m - 1)

sol = Solution()
print(sol.uniquePaths(3, 7))
print(sol.uniquePaths(3, 2))
