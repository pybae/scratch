from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged_intervals = [intervals[0]]

        for i in range(1, len(intervals)):
            if self.overlap(merged_intervals[-1], intervals[i]):
                merged_intervals[-1] = self.merge_intervals(merged_intervals[-1], intervals[i])
            else:
                merged_intervals.append(intervals[i])

        return merged_intervals

    def overlap(self, a: List[int], b: List[int]) -> bool:
        return a[0] <= b[0] <= a[1] or b[0] <= a[1] <= b[1]
    
    def merge_intervals(self, a: List[int], b: List[int]) -> List[int]:
        return [min(a[0], b[0]), max(a[1], b[1])]

sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
print(sol.merge([[1,4],[4,5]]))
