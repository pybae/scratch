from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = nums[0], 0
        for num in nums[1:]:
            count += 1 if candidate == num else -1
            if count == 0:
                candidate = num

        return candidate

sol = Solution()
print(sol.majorityElement([3, 2, 3]))
print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))
