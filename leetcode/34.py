from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        low_index = self.searchLeft(nums, target, 0, len(nums) - 1)
        right_index = self.searchRight(nums, target, low_index, len(nums) - 1)
        return [low_index, right_index]


    def searchLeft(self, nums, target, i, j) -> int:
        if j < i or i < 0 or j >= len(nums):
            return -1

        mid = (i + j) // 2
        print(i, j, mid)


        if nums[mid] == target:
            return mid
        elif i == mid:
            return -1
        elif target < nums[mid]:
            return self.searchLeft(nums, target, i, mid - 1)
        else:
            return self.searchLeft(nums, target, mid, j)

    def searchRight(self, nums, target, i, j) -> int:
        if j < i or i < 0 or j >= len(nums):
            return -1


        mid = (i + j + 1) // 2
        print(i, j, mid)

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.searchRight(nums, target, mid + 1, j)
        else:
            return self.searchRight(nums, target, i, mid -1)



sol = Solution()
print(sol.searchRange([5,7,7,8,8,10], 8))
print(sol.searchRange([5,7,7,8,8,10], 6))
print(sol.searchRange([], 0))
