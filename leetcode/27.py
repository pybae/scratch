from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums) - 1

        while i <= j:
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                i += 1

        return i

sol = Solution()
print(sol.removeElement([3,2,2,3], 3))
print(sol.removeElement([0,1,2,2,3,0,4,2], 2))
