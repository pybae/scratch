from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i, left, right = 0, 0, len(nums) - 1
        while i <= right:
            print(nums)
            if nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            elif nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                i += 1
                left += 1
            else:
                i += 1
        return 


sol = Solution()
a = [1, 2, 0]
sol.sortColors(a)
print(a)
