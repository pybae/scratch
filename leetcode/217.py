from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False

sol = Solution()
print(sol.containsDuplicate([1, 2, 3, 1]))
print(sol.containsDuplicate([1, 2, 3 ,4]))
print(sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
