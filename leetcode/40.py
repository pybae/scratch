from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, 0, target, [], res)
        return res

    def dfs(self, candidates: List[int], index: int, target: int, path: List[int], result:
            List[List[int]]):
        i = index
        while i < len(candidates):
            candidate = candidates[i]
            if candidate == target:
                path.append(candidate)
                result.append(list(path))
                path.pop()
            elif candidate < target:
                path.append(candidate)
                self.dfs(candidates, i + 1, target - candidate, path, result)
                path.pop()
            else:
                break

            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            i += 1

        return


sol = Solution()
# 1, 1, 2, 5, 6, 7, 10
print(sol.combinationSum2([10,1,2,7,6,1,5], 8))
