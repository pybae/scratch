class Solution:
    def flatten(self, arr):
        res = ""
        for row in arr:
            for char in row:
                if char != 0:
                    res += char
        return(res)

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        arr = [[0 for i in range(len(s))] for j in range(numRows)]

        i = 0
        j = 0
        for c in s:
            arr[i][j] = c

            if j % (numRows - 1) == 0:
                # means fill column
                if i < numRows - 1:
                    i += 1
                else:
                    i -= 1
                    j += 1
            else:
                # means zig zag up
                i -= 1
                j += 1

        return self.flatten(arr)


sol = Solution()
print(sol.convert("PAYPALISHIRING", 3))
print(sol.convert("PAYPALISHIRING", 4))
print(sol.convert("PAYPALISHIRING", 1))
