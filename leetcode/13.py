
class Solution:
    symbols = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
            }

    def romanToInt(self, s: str) -> int:
        result = 0

        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in self.symbols:
                result += self.symbols[s[i:i+2]] 
                i += 2
            else:
                result += self.symbols[s[i]]
                i += 1

        return result

sol = Solution()
print(sol.romanToInt("III"))
print(sol.romanToInt("LVIII"))
print(sol.romanToInt("MCMXCIV"))
