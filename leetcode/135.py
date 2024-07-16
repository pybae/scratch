import math
from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        boundaries at ends are basically infinity for both
        so append that to both, perhaps even could to simplify the code

        if you are less than both of your neighbors, give one
        if you are less than your left neighbor, but greater than your right,
        keep iterating until you find the valley.

        then count backwards from that

        if you are greater than your left neighbor, but less than your right
        give one more than what he got, and go forth
        """

        candies = [1] * len(ratings)
        ratings = [math.inf] + ratings + [math.inf]

        i = 1
        while i < len(ratings) - 1:
            if ratings[i - 1] >= ratings[i] <= ratings[i + 1]:
                candies[i - 1] = candies[i - 1]
            elif ratings[i - 1] < ratings[i]:
                candies[i - 1] = candies[i - 2] + 1
            elif ratings[i] > ratings[i + 1]:
                j = i
                while ratings[j] > ratings[j + 1]:
                    j += 1
                
                count = 1
                while j >= i:
                    candies[j - 1] = count
                    j -= 1
                    count += 1
                i += count - 2
            i += 1

        return sum(candies)

sol = Solution()
print(sol.candy([4, 3, 2, 1, 2, 3]))
print(sol.candy([1, 0, 2]))
print(sol.candy([1, 2, 2]))
