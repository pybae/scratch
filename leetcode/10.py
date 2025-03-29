
class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        """
        Wait so how do you do this again real quick?
        you do need two
        so , aa, a progress a, ""A


        okay os what's the reiterative case, like the thing

        uhhh aaaaaab, a*ab

        yeah i mean if you constrain s and p it'll work
        max is that right
        yeah the other ones should stop going since it realizes that. i think

        right, starting from the second character, you wouldn't reuse the results of the first
        """

        dp = [[None for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        return self.recurse(s, p, 0, 0, dp)

    def recurse(self, s: str, p: str, i: int, j: int, dp: list[list[bool]]) -> bool:
        if dp[i][j] != None:
            return

        if dp[i][j] is not None:
            return dp[i][j]

        if j == len(p):
            dp[i][j] = i == len(s)
            return dp[i][j]

        match = i < len(s) and (s[i] == p[j] or p[j] == '.')

        if (j + 1) < len(p) and p[j + 1] == '*':
            dp[i][j] = (
                self.recurse(s, p, i, j + 2, dp) or
                (match and self.recurse(s, p, i + 1, j, dp))
            )
        else:
            dp[i][j] = match and self.recurse(s, p, i + 1, j + 1, dp)

        return dp[i][j]


sol = Solution()
print(sol.isMatch("aa", "a"))
print(sol.isMatch("aa", "a*"))
print(sol.isMatch("ab", ".*"))
print(sol.isMatch("aaaab", ".*ab"))
