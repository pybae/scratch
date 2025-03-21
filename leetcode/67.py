
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        i, carry = 0, 0

        result = ""
        while i < len(a) and i < len(b):
            res = int(a[i]) + int(b[i]) + carry
            result += "1" if res % 2 else "0"
            carry = int(res >= 2)
            i += 1

        
        leftover = a[i:] or b[i:]
        for num in leftover:
            res = int(num) + carry
            result += "1" if res % 2 else "0"
            carry = int(res >= 2)

        if carry:
            result += "1"

        return result[::-1]

sol = Solution()
print(sol.addBinary("11", "1"))
print(sol.addBinary("1010", "1011"))
