# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return version >= 4

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n

        while l < r:
            mid = l + (r - l) // 2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l


sol = Solution()
print(sol.firstBadVersion(5))
print(sol.firstBadVersion(10))
