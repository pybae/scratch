from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged_intervals = []
        intervals.sort(key=lambda x: x[0])

        i = 0
        while i < len(intervals):
            interval_start, interval_end = intervals[i][0], intervals[i][1]

            j = i + 1
            while j < len(intervals) and intervals[j][0] <= interval_end:
                interval_end = max(interval_end, intervals[j][1])
                j += 1

            if j - i > 1:
                merged_intervals.append([interval_start, interval_end])
                i = j
            else:
                merged_intervals.append(intervals[i])
                i += 1

        return merged_intervals

sol = Solution()
print(sol.merge([[1,4],[2, 3]]))
