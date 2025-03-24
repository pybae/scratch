from collections import deque
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        original_color = image[sr][sc]
        q = deque([(sr, sc)])
        while q:
            i, j = q.popleft()

            if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]):
                continue

            if image[i][j] == original_color:
                image[i][j] = color
                q.append((i - 1, j))
                q.append((i + 1, j))
                q.append((i, j - 1))
                q.append((i, j + 1))

        return image

