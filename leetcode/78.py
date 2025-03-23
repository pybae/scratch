from typing import List
from collections import deque

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        if len(nums) == 1:
            return [[], nums]

        result = [[]]
        for i in range(len(nums)):
            result.extend([nums[i]] + subset for subset in self.subsets(nums[i + 1:]))

        return result

sol = Solution()
print(sol.subsets([0]))
