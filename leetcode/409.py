class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1

        has_odd = any(count % 2 == 1 for count in counts.values())
        return sum((count // 2) * 2 for count in counts.values()) + has_odd

sol = Solution()
print(sol.longestPalindrome("abccccdd"))
print(sol.longestPalindrome("bb"))
print(sol.longestPalindrome("a"))
