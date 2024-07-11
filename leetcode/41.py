from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        j = self.filterNonPositives(nums)
        j = self.filterOutOfBounds(nums, j)

        for num in nums[:j]:
            nums[num - 1] = num

        s = 1
        for num in nums:
            if num != s:
                return s
            s += 1

        return s

    # returning the count of # non positives
    def filterNonPositives(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] <= 0:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j -= 1
            else:
                i += 1
        return j

    # returning the count of # numbers out of bounds
    def filterOutOfBounds(self, nums: List[int], j) -> int:
        m = j + 1
        i = 0
        while i <= j:
            if nums[i] > m:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j -= 1
            else:
                i += 1
        return j + 1

    # def sortByIndex(self, filtered_nums: List[int], nums: List[int]) -> int:



sol = Solution()
print(sol.firstMissingPositive([1, 2, 0]))
print(sol.firstMissingPositive([3, 4, -1, 1]))
print(sol.firstMissingPositive([-2, -10, 3, -10, 3, 4, -1, 1]))
print(sol.firstMissingPositive([7, 8, 11, 12, 9]))
