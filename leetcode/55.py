from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos = 0
        while pos + nums[pos] < len(nums) - 1:
            next_pos, max_reach = pos, nums[pos] + pos

            for i in range(0, nums[pos] + 1):
                if nums[pos + i] + pos + i > max_reach:
                    max_reach = nums[pos + i] + pos + i
                    next_pos = pos + i

            if pos == next_pos:
                return False
            pos = next_pos

        return True

sol = Solution()
print(sol.canJump([2,3,1,1,4]))
print(sol.canJump([3,2,1,0,4]))
print(sol.canJump([1,1,1,0]))
print(sol.canJump([1,1,2,2,0,1,1]))

