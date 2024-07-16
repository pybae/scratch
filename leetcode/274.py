from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()

        h_index = 0
        for i in range(len(citations) - 1, -1, -1):
            if citations[i] > h_index and len(citations) - i > h_index:
                h_index += 1


        return h_index

sol = Solution()
print(sol.hIndex([3,0,6,1,5]))
print(sol.hIndex([1, 1, 1, 5, 6]))
print(sol.hIndex([1,3,1]))
