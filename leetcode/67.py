class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) -1

        result = ""
        carry = False
        while i >= 0 or j >= 0:
            add_i = i >= 0 and a[i] == "1"
            add_j = j >= 0 and b[j] == "1"
            
            ones = int(add_i) + int(add_j) + int(carry)
            if ones == 3:
                result = "1" + result
                carry = True
            elif ones == 2:
                result = "0" + result
                carry = True
            elif ones == 1:
                carry = False
                result = "1" + result
            else:
                carry = False
                result = "0" + result

            i -= 1
            j -= 1

        if carry:
            return "1" + result
        return result

sol = Solution()
print(sol.addBinary("11", "1"))
print(sol.addBinary("1010", "1011"))
