import math

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        best_sum = math.inf
        nums.sort()

        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1

            while j < k:
                cur = nums[i] + nums[j] + nums[k]
                if abs(target - cur) < abs(target - best_sum):
                    best_sum = cur

                if cur < target:
                    j += 1
                else:
                    k -= 1

        return best_sum

sol = Solution()
print(sol.threeSumClosest([-1,2,1,-4], 1))
print(sol.threeSumClosest([0,0,0], 1))
