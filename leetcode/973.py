from typing import List
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)):
            x, y = points[i]
            points[i].append(math.sqrt(x**2 + y**2))
        points.sort(key=lambda x: x[2])

        return [[point[0], point[1]] for point in points[0:k]]

sol = Solution()
print(sol.kClosest([[1,3],[-2,2]], 1))
print(sol.kClosest([[3,3],[5,-1],[-2,4]], 2))
