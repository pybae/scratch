class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        
        neg = False
        if x < 0:
            neg = True
            x *= -1

        while x != 0:
            ans *= 10
            ans += x % 10
            x //= 10

        if abs(ans) > 2147483647:
            return 0
        if neg:
            return -ans
        else:
            return ans

sol = Solution()
print(sol.reverse(123))
print(sol.reverse(-123))
print(sol.reverse(120))
print(sol.reverse(1563847412))
