from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = {}
        for i, num in enumerate(nums):
            num_set[num] = i

        for i, num in enumerate(nums):
            if (target - num) in num_set and num_set[target - num] != i:
                return [i, num_set[target - num]]

        return []



sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
print(sol.twoSum([3, 2, 4], 6))
print(sol.twoSum([3, 3], 6))
