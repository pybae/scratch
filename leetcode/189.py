from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        i, nums_rotated = 0, 0
        while nums_rotated < len(nums):
            j = (i + k) % len(nums)
            nums_rotated += 1
            while j != i:
                nums[i], nums[j] = nums[j], nums[i]
                j = (j + k) % len(nums)
                nums_rotated += 1

            i += 1

        return nums


sol = Solution()
nums = [1,2,3,4,5,6,7]
sol.rotate(nums, 3)
print(nums)

nums = [-1, -100, 3, 99]
sol.rotate(nums, 2)
print(nums)
