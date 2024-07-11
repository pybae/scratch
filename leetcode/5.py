class Solution:
    def expand(self, s: str, j: int, k: int) -> str:
        while 0 <= j and k < len(s) and s[j] == s[k]:
            j -= 1
            k += 1
        return s[j + 1: k]


    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i, c in enumerate(s):
            sub1 = self.expand(s, i, i)
            sub2 = self.expand(s, i, i + 1)

            if len(ans) < len(sub1):
                ans = sub1
            if len(ans) < len(sub2):
                ans = sub2

        return ans


sol = Solution()
print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome("cbbd"))
