from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_start, col_start, row_end, col_end = 0, 0, len(matrix) - 1, len(matrix[0]) - 1

        result = []
        while row_start <= row_end and col_start <= col_end:
            print(row_start, row_end, col_start, col_end)
            print(result)
            for i in range(col_start, col_end + 1):
                result.append(matrix[row_start][i])
            row_start += 1

            for i in range(row_start, row_end + 1):
                result.append(matrix[i][col_end])
            col_end -= 1

            if row_start <= row_end:
                for i in range(col_end, col_start - 1, -1):
                    result.append(matrix[row_end][i])
                row_end -= 1

            if col_start <= col_end:
                for i in range(row_end, row_start - 1, -1):
                    result.append(matrix[i][col_start])
                col_start += 1

        return result

sol = Solution()
print(sol.spiralOrder([[1, 2, 3]]))
print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
# print(sol.spiralOrder([[1], [2]]))
