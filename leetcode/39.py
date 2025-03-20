from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [None] * (target + 1)
        candidates.sort()
        for i in range(target + 1):
            dp[i] = []
            for num in candidates:
                if num > i:
                    break
                elif num == i:
                    dp[i].append([num])
                elif dp[i - num]:
                    dp[i].extend(c + [num] for c in dp[i - num])
            dp[i] = [list(x) for x in list(set([tuple(sorted(c)) for c in dp[i]]))]
        return dp[target]


sol = Solution()
print(sol.combinationSum([2, 3, 6, 7], 7))
print(sol.combinationSum([8, 7, 4, 3], 11))
print(sol.combinationSum([2, 3, 5], 8))
print(sol.combinationSum([2], 1))
