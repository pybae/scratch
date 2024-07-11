from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.dfs(nums, 0, result)
        return result

    def dfs(self, nums, i, result):
        if i == len(nums) - 1:
            result.append(list(nums))
            return 

        for j in range(i, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            self.dfs(nums, i + 1, result)
            nums[i], nums[j] = nums[j], nums[i]


sol = Solution()
print(sol.permute([1, 2, 3]))
print(sol.permute([0, 1]))
print(sol.permute([1]))
