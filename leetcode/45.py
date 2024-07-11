from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        i, jumps = 0, 0

        while i < len(nums) - 1:
            if nums[i] + i >= len(nums) - 1:
                return jumps + 1

            max_reach = i
            j, next_i = i, i

            while j <= nums[i] + i and j < len(nums):
                reach = nums[j] + j
                if reach >= max_reach:
                    next_i = j
                    max_reach = reach
                j += 1

            i = next_i
            jumps += 1

        return jumps

sol = Solution()
print(sol.jump([1, 2, 3]))
