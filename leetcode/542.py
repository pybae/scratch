from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        d = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    d.append((i, j))
                else:
                    mat[i][j] = -1

        while d:
            i, j = d.popleft()
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for di, dj in directions:
                if 0 <= i + di < len(mat) and 0 <= j + dj < len(mat[0]) and mat[i + di][j + dj] == -1:
                    mat[i + di][j + dj] = mat[i][j] + 1
                    d.append((i + di), (j + dj))

        return d
