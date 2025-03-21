from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        for i in range(min(len(matrix), len(matrix[0])) // 2 + 1):
            result += self.spiral(matrix, i)
        return result
    
    def spiral(self, matrix: List[List[int]], layer: int) -> List[int]:
        result = []
        matrix = [row[layer: len(row) - layer] for row in matrix[layer:len(matrix) - layer]]

        result.extend(matrix[0])
        result.extend([matrix[i][-1] for i in range(1, len(matrix)) if len(matrix[i]) > 0])
        result.extend(matrix[-1][-2::-1] if len(matrix) > 1 else [])
        result.extend([matrix[i][0] for i in range(len(matrix) - 2, 0, -1) if len(matrix[i]) > 0])

        return result

sol = Solution()
print(sol.spiralOrder([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))

print(sol.spiralOrder([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]))

print(sol.spiralOrder([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
]))

print(sol.spiralOrder([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20],
    [21, 22, 23, 24]
]))
