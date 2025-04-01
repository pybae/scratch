from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        next lexicographically greater pemutation
        """

        if len(nums) <= 1:
            return nums

        # starting from back, see if there's a place to swap
        i = len(nums) - 1
        while i > 0:
            if nums[i - 1] < nums[i]:
                break
            i -= 1

        # fully in reverse order, so return reverse
        if i == 0:
            nums[0::] = nums[::-1]
            return

        min_index = i
        for j in range(i, len(nums)):
            if nums[j] > nums[i - 1]:
                min_index = j

        nums[i - 1], nums[min_index] = nums[min_index], nums[i - 1]
        nums[i::] = nums[i::][::-1]
        return
        
sol = Solution()
a = [1, 2, 3]
sol.nextPermutation(a)
print(a)

sol.nextPermutation(a)
print(a)

sol.nextPermutation(a)
print(a)

sol.nextPermutation(a)
print(a)

sol.nextPermutation(a)
print(a)

sol.nextPermutation(a)
print(a)
