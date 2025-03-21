class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        prev, cur = 1, 2
        for i in range(n - 2):
            cur, prev = cur + prev, cur

        return cur


