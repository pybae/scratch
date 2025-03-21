from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]

        permutations = []
        for i in range(len(nums)):
            nums[0], nums[i] = nums[i], nums[0]
            permutations.extend([nums[0]] + x for x in self.permute(nums[1:]))
            nums[0], nums[i] = nums[i], nums[0]
        return permutations

sol = Solution()
print(sol.permute([1, 2, 3]))
