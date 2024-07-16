from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diffs = [gas[i] - cost[i] for i in range(len(gas))]

        if sum(diffs) < 0:
            return -1

        diffs = diffs + diffs
        best_starting_point, current_sum = 0, 0

        for i in range(len(gas)):
            if current_sum == 0 and diffs[i] > 0:
                best_starting_point = i
            current_sum = max(0, current_sum + diffs[i])

        return best_starting_point


sol = Solution()
print(sol.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
print(sol.canCompleteCircuit([2, 3, 4], [3, 4, 3]))
"""

  [1, 2, 3, 4, 5]
- [3, 4, 5, 1, 2]

  [-2, -2, -2, 3, 3]

  [4, -2, 6, -10, 2]

  [2, 3, 4]
  [3, 4, 3]
- [-1, -1, 1]

"""
