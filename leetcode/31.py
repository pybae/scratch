from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # so the intuition is you want to find where the shift occurs and the
        # rest is a monotonically decreasing list
        # for 1, 3, 2, that's 1 -> [3, 2], [2, 3]
        # for 2, 1, 3 that's 2 -> [1, 3], [3, 1]
        return 

sol = Solution()
a = [1, 3, 2]
sol.nextPermutation(a)
print(a)

a = [1, 2, 3]
sol.nextPermutation(a)
print(a)

a = [3, 2, 1]
sol.nextPermutation(a)
print(a)

a = [1, 1, 5]
sol.nextPermutation(a)
print(a)
