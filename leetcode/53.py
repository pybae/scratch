from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = current_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum += nums[i]
            current_sum = max(nums[i], current_sum)
            max_sum = max(current_sum, max_sum)

        return max_sum


sol = Solution()
print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(sol.maxSubArray([5, 4, -1, 7, 8]))
