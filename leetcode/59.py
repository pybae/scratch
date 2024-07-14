from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        count = 1
        result = [[0 for i in range(0, n)] for i in range(0, n)]
        layer = 0
        while layer < (n + 1) // 2:
            for i in range(layer, n - layer):
                result[layer][i] = count
                count += 1
            for i in range(layer + 1, n - layer):
                result[i][n - layer - 1] = count
                count += 1
            for i in range(n - layer - 2, layer - 1, -1):
                result[n - layer - 1][i] = count
                count += 1
            for i in range(n - layer - 2, layer, -1):
                result[i][layer] = count
                count += 1
            layer += 1

        return result

sol = Solution()
m = sol.generateMatrix(1)
for row in m:
    print(row)

"""

1  2  3  4  5
16 17 18    6
15          7
14          8
13 12 11 10 9

"""
