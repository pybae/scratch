from typing import List

class Solution:
    digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            }

    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        for digit in digits:
            if ans:
                new_ans = []
                for a in ans:
                    new_ans += [a + letter for letter in Solution.digit_to_letters[digit]]
                ans = new_ans
            else:
                ans = [letter for letter in Solution.digit_to_letters[digit]]

        return ans

sol = Solution()
print(sol.letterCombinations("23"))
print(sol.letterCombinations(""))
print(sol.letterCombinations("2"))
