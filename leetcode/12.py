
class Solution:
    symbols = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M"
    }

    def intToRoman(self, num: int) -> str:
        result = ""

        while num:
            value_to_subtract = None
            for value in sorted(self.symbols.keys())[::-1]:
                if value <= num:
                    value_to_subtract = value
                    break

            num -= value_to_subtract
            result += self.symbols[value_to_subtract]

        return result


sol = Solution()
print(sol.intToRoman(3749))
print(sol.intToRoman(58))
print(sol.intToRoman(1994))
