from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        if not intervals:
            return [new_interval]

        i = j = self.find_overlapping_interval(intervals, new_interval)

        while j < len(intervals) and self.overlaps(intervals[j], new_interval):
            new_interval = self.merge(intervals[j], new_interval)
            j += 1

        if i == j:
            intervals.insert(i + 1, new_interval)
        else:
            intervals[i:j] = [new_interval]
        return intervals

    def find_overlapping_interval(self, intervals: List[List[int]], new_interval: List[int]) -> int:
        l, r = 0, len(intervals) - 1
        while l <= r:
            mid = (l + r) // 2
            if intervals[mid][0] <= new_interval[0] <= intervals[mid][1]:
                return mid
            elif intervals[mid][0] > new_interval[0]:
                r = mid - 1
            else:
                l = mid + 1
        
        return l if new_interval[0] < intervals[mid][0] else r

    def overlaps(self, a: List[int], b: List[int]) -> bool:
        return max(a[0], b[0]) <= min(a[1], b[1])

    def merge(self, a: List[int], b: List[int]) -> List[int]:
        return [min(a[0], b[0]), max(a[1], b[1])]

sol = Solution()
# print(sol.insert([[1,3],[6,9]], [4,5]))
# print(sol.insert([[1,3],[6,9]], [2,5]))
# print(sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
# print(sol.insert([], [5, 7]))
print(sol.insert([[2, 3], [5, 7]], [0, 6]))
print(sol.insert([[1, 5]], [0, 0]))
