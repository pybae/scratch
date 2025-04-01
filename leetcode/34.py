from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1 and nums[0] == target:
            return [0, 0]

        left_side = self.search_val(nums, target)
        right_side = self.search_val(nums, target + 1)
        
        if nums[left_side] == target and nums[right_side] == target:
            return [left_side, right_side]
        elif nums[left_side] == target and nums[right_side - 1] == target:
            return [left_side, right_side - 1]
        else:
            return [-1, -1]

    def search_val(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        return l


sol = Solution()
print(sol.searchRange([5,7,7,8,8,10], 8))
print(sol.searchRange([5,7,7,8,8,10], 6))
print(sol.searchRange([1], 1))
print(sol.searchRange([2,2], 2))
