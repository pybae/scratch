class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            return self.rle(self.countAndSay(n - 1))

    def rle(self, s: str) -> str:
        result = ""

        current_char = s[0]
        current_count = 0
        for c in s:
            if current_char == c:
                current_count += 1
            else:
                result += str(current_count) + current_char
                current_count = 1
                current_char = c
        result += str(current_count) + current_char
        return result
            


sol = Solution()
print(sol.rle("1"))
print(sol.rle("3322251"))
print(sol.countAndSay(1))
print(sol.countAndSay(4))
