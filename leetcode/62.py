from math import perm

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return perm(m + n - 2, 2) // 2

sol = Solution()
print(sol.uniquePaths(3, 2))
print(sol.uniquePaths(3, 7))
