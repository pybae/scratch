from typing import List

OPERATORS = set(["+", "-", "*", "/"])
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in OPERATORS:
                a, b = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(b - a)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(int(b / a))
            else:
                stack.append(int(token))
        return stack.pop()

sol = Solution()

print(sol.evalRPN(["2","1","+","3","*"]))
print(sol.evalRPN(["4","13","5","/","+"]))
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
