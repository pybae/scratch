from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()

        for i in range(len(nums) - 1):
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    result.add((nums[i], nums[j], nums[k]))
                    j += 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1

        return [[t[0], t[1], t[2]] for t in result]

sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
