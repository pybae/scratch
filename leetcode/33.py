from typing import List

class Solution:
    """
    4, 5, 6, 7, 0, 1, 2

    7, 0, 1, 2, 4, 5, 6,
    target is 3

    """
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            if l == r and nums[l] != target:
                return -1

            # are we sorted?
            if nums[l] < nums[r]:
                # if so, normal binary search
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # one of the two sides must be sorted
                if nums[l] <= nums[mid]:
                    # left side sorted
                    if nums[l] <= target <= nums[mid]:
                        r = mid - 1
                    else:
                        l = mid + 1
                else:
                    # right side sorted
                    if nums[mid] <= target <= nums[r]:
                        l = mid + 1
                    else:
                        r = mid - 1

                
        return -1

sol = Solution()
print(sol.search([3, 1], 1))
