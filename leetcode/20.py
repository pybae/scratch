class Solution:
    brackets = {
        "(": ")",
        "[": "]",
        "{": "}"
    }

    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in self.brackets:
                stack.append(char)
            elif not stack or char != self.brackets[stack.pop()]:
                return False
        return not stack 

sol = Solution()
print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("([])"))
print(sol.isValid("([)]"))
