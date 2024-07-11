from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.search_helper(nums, 0, len(nums) - 1, target)

    def search_helper(self, nums: List[int], i: int, j: int, target: int) -> int:
        if i == j:
            if target == nums[i]:
                return i
            else:
                return -1

        mid = ((j - i) // 2) + i

        if nums[mid] == target:
            return mid
        elif nums[i] <= nums[mid]:
            if nums[i] <= target <= nums[mid]:
                return self.search_helper(nums, i, mid, target)
            else:
                return self.search_helper(nums, mid + 1, j, target)
        else:
            if nums[mid] <= target <= nums[j]:
                return self.search_helper(nums, mid, j, target)
            else:
                return self.search_helper(nums, i, mid - 1, target)


# 0, 6
# 4, 6
# 
sol = Solution()
print(sol.search([1, 3], 0))
