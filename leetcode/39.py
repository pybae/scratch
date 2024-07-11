from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.combinationSumRecursive(candidates, target)

    def combinationSumRecursive(self, candidates, target):
        result = []
        for candidate in candidates:
            if candidate == target:
                result += [[target]]
            elif candidate < target:
                subresults = self.combinationSumRecursive(candidates, target - candidate)
                for subresult in subresults:
                    subresult.append(candidate)
                    result.append(subresult)
            else:
                break

        return result


sol = Solution()
print(sol.combinationSum([2, 3, 6, 7], 7))
# print(sol.combinationSum([2, 3, 5], 8))
# print(sol.combinationSum([2], 1))
