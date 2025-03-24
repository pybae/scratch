class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")

        stack = []
        current_sum = 0
        current_sign = 1
        number = 0

        i = 0
        while i < len(s):
            c = s[i]

            if c.isdigit():
                number = number * 10 + int(c)
            elif c in '+-':
                current_sum += current_sign * number
                number = 0
                current_sign = 1 if c == '+' else -1
            elif c == '(':
                stack.append((current_sum, current_sign))
                current_sum, current_sign = 0, 1
            elif c == ')':
                current_sum += current_sign * number
                number = 0

                prev_sum, prev_sign = stack.pop()
                current_sum = prev_sum + (prev_sign * current_sum)

            i += 1

        current_sum += current_sign * number
        return current_sum


# Test
sol = Solution()
expr = "(1+(4+5+2)-3)+(6+8)"
print(sol.calculate(expr))  # 23

