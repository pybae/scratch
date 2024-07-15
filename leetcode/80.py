from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        while j < len(nums):
            k = j
            while j < len(nums) and nums[k] == nums[j]:
                j += 1

            if j - k >= 2:
                nums[i] = nums[k]
                nums[i + 1] = nums[k + 1]
                i += 2
            else:
                nums[i] = nums[k]
                i += 1

        return i


sol = Solution()
nums = [1,1,1,2,2,3]
print(sol.removeDuplicates(nums))
print(nums)

nums = [0,0,1,1,1,1,2,3,3]
print(sol.removeDuplicates(nums))
print(nums)
