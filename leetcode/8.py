class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0

        i = 0
        neg = False

        if s[0] == "-":
            neg = True
            i += 1
        elif s[0] == "+":
            i += 1

        res = 0
        while i < len(s) and s[i].isdigit():
            res *= 10
            res += int(s[i])
            i += 1

        
        if neg:
            return max(-res, -(2**31))
        else:
            return min(res, (2**31) - 1)


sol = Solution()
print(sol.myAtoi("42"))
print(sol.myAtoi("  -042"))
print(sol.myAtoi("1337c0d3"))
print(sol.myAtoi("0-1"))
print(sol.myAtoi("words and 987"))
