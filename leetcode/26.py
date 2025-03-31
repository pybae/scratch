from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1

        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[j] = nums[i]
                j += 1

        return j

sol = Solution()
print(sol.removeDuplicates([1,1,2]))
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
