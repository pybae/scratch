from typing import List

class Solution:
    def trap(self, heights: List[int]) -> int:
        res = 0

        accum, height = 0, heights[0]
        for i in range(1, len(heights)):
            if heights[i] >= height:
                res += accum
                accum, height = 0, heights[i]
            else:
                accum += height - heights[i]

        accum, height = 0, heights[-1]
        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > height:
                res += accum
                accum, height = 0, heights[i]
            else:
                accum += height - heights[i]

        return res


sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(sol.trap([4,2,0,3,2,5]))
