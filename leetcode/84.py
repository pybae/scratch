from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        so the stack is monotonically increasing


        i see - only need to check max area when going down, so just append that and clean up the fuck out of it.
        elegant ish eh.
        """

        # list of index, height
        s: list[tuple[int, int]] = [(0, heights[0])]

        # index in stack to check
        previous_max = 0
        max_size = heights[0]

        for i in range(1, len(heights)):
            if heights[i] > s[-1][1]:
                s.append((i, heights[i]))
            elif heights[i] < s[-1][1]:
                left = s.pop()
                while s and s[-1][1] >= heights[i]:
                    max_size = max(max_size, (i - left[0]) * left[1])
                    left = s.pop()

                max_size = max(max_size, (i - left[0]) * left[1])
                s.append((left[0], min(left[1], heights[i])))
                max_size = max(max_size, (i - s[-1][0] + 1) * s[-1][1])
            else:
                max_size = max(max_size, (i - s[-1][0] + 1) * s[-1][1])

        left = s.pop()
        while s:
            max_size = max(max_size, (i - left[0] + 1) * left[1])
            left = s.pop()

        return max_size

sol = Solution()
print(sol.largestRectangleArea([2,1,5,6,2,3]))
print(sol.largestRectangleArea([2,4]))
print(sol.largestRectangleArea([1,2,2]))
print(sol.largestRectangleArea([4,2,0,3,2,5]))
print(sol.largestRectangleArea([0,1,0,2,1,0,1,3,2,1,2,1]))
print(sol.largestRectangleArea([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]))
print(sol.largestRectangleArea([5,3,6,3,6,8,6,1,6,2,0]))
print(sol.largestRectangleArea([5,7,0,7,2,9,2,7,6,8,8]))
