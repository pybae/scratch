class Solution:
    def longestPalindrome(self, s: str) -> str:
        i, result = 0, ""
        while i < len(s):
            j = self.expandToSameCharacters(s, i)
            palindrome = self.expandPalindrome(s, i, j)

            if len(palindrome) > len(result):
                result = palindrome

            i = j + 1

        return result

    def expandToSameCharacters(self, s: str, i: int) -> int:
        while i + 1 < len(s) and s[i + 1] == s[i]:
            i += 1
        return i

    def expandPalindrome(self, s: str, i: int, j: int) -> str:
        while i > 0 and j < len(s) - 1 and s[i - 1] == s[j + 1]:
            i -= 1
            j += 1
        return s[i:j+1]


sol = Solution()
print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome("babab"))
print(sol.longestPalindrome("cbbd"))
