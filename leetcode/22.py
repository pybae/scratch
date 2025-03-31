from typing import List

class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        
        result = set()
        for prior in self.generateParenthesis(n - 1):
            for i in range(len(prior)):
                result.add(prior[:i] + "()" + prior[i:])

        return list(result)

sol = Solution()
print(sol.generateParenthesis(3))
print(sol.generateParenthesis(2))
print(sol.generateParenthesis(1))
