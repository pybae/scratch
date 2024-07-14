
class Solution:
    def isNumber(self, s: str) -> bool:
        return self.isInteger(s) or self.isDecimal(s)

    def isInteger(self, s: str) -> bool:
        if len(s) == 0:
            return False

        i = 0
        if s[0] == "-" or s[0] == "+":
            i += 1

        found_digit = False

        while i < len(s):
            if s[i] == "e" or s[i] == "E":
                break
            elif s[i].isdigit():
                found_digit = True
            else:
                return False
            i += 1

        if not found_digit:
            return False
        elif i == len(s):
            return True
        else:
            if "e" not in s[i + 1:]:
                return self.isInteger(s[i + 1:]) # validate the exponent
            else:
                return False

    def isDecimal(self, s: str) -> bool:
        if len(s) == 0:
            return False

        i = 0
        if s[0] == "-" or s[0] == "+":
            i += 1

        found_digit = False
        found_dot = False
        while i < len(s):
            if s[i] == "e" or s[i] == "E":
                break
            if s[i] == ".":
                if found_dot:
                    return False
                found_dot = True
            elif s[i].isdigit():
                found_digit = True
            else:
                return False
            i += 1

        if not found_dot or not found_digit:
            return False
        elif i == len(s):
            return True
        else:
            if "e" not in s[i + 1:]:
                return self.isInteger(s[i + 1:]) # validate the exponent
            else:
                return False


sol = Solution()
print(sol.isNumber("2"))
print(sol.isNumber("0089"))
print(sol.isNumber("-0.1"))
print(sol.isNumber("+3.14"))
print(sol.isNumber("+3.14"))
print(sol.isNumber("4."))
print(sol.isNumber("-.9"))
print(sol.isNumber("2e10"))
print(sol.isNumber("-90E3"))
print(sol.isNumber("+6e-1"))
print(sol.isNumber("53.5e93"))
print(sol.isNumber("-123.456e789"))
print(sol.isNumber("92e1740e91"))
# print(sol.isNumber("abc"))
# print(sol.isNumber("1a"))
# print(sol.isNumber("1e"))
# print(sol.isNumber("e3"))
# print(sol.isNumber("99e2.5"))
# print(sol.isNumber("--6"))
# print(sol.isNumber("-+3"))
# print(sol.isNumber("95a54e53"))
# print(sol.isNumber("."))

