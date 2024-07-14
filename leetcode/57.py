from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        added = False
        if len(intervals) == 0:
            return [newInterval]

        for interval in intervals:
            if newInterval[0] <= interval[0] <= newInterval[1] or interval[0] <= newInterval[0] <= interval[1]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
            elif newInterval[1] <= interval[0] and not added:
                added = True
                result.append(newInterval)
                result.append(interval)
            else:
                result.append(interval)

        if not added:
            result.append(newInterval)
        return result

sol = Solution()
print(sol.insert([[2,5],[6,7],[8,9]], [0, 1]))
