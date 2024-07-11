from typing import List

class Solution:
    def trap(self, heights: List[int]) -> int:
        return self.scanLeft(heights) + self.scanRight(heights)

    def scanLeft(self, heights: List[int]) -> int:
        result = 0
        left, accum = 0, 0
        for i, height in enumerate(heights):
            if heights[i] >= heights[left]:
                result += accum
                accum = 0
                left = i
            else:
                accum += heights[left] - heights[i]
        return result


    def scanRight(self, heights: List[int]) -> int:
        heights.reverse()
        result = 0
        left, accum = 0, 0
        for i, height in enumerate(heights):
            if heights[i] > heights[left]:
                result += accum
                accum = 0
                left = i
            else:
                accum += heights[left] - heights[i]
        return result


sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(sol.trap([4,2,0,3,2,5]))
print(sol.trap([2, 0, 2]))
