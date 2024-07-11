class Solution:
    def isPalindrome(self, x: int) -> bool:
        s_x = str(x)

        for i in range(len(s_x) // 2):
            if s_x[i] != s_x[len(s_x) - i -1]:
                return False

        return True

sol = Solution()
print(sol.isPalindrome(121))
print(sol.isPalindrome(-121))
print(sol.isPalindrome(10))
