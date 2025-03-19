from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                second, first = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(first - second)
                elif token == "*":
                    stack.append(first * second)
                elif token == "/":
                    stack.append(int(first / second))
            else:
                stack.append(int(token))
        return stack[0]

sol = Solution()
print(sol.evalRPN(["2","1","+","3","*"]))
print(sol.evalRPN(["3","1","-"]))
print(sol.evalRPN(["4","13","5","/","+"]))
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
