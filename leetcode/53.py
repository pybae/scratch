from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum, max_sum = max(0, nums[0]), nums[0]

        for num in nums[1:]:
            current_sum += num
            if current_sum < 0:
                max_sum = max(max_sum, num)
                current_sum = 0
            else:
                max_sum = max(max_sum, current_sum)

        return max_sum


sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(sol.maxSubArray([1]))
print(sol.maxSubArray([5, 4, -1, 7, 8]))
print(sol.maxSubArray([-2, 1]))
print(sol.maxSubArray([-2, -1,]))
