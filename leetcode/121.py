from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 1:
            return 0

        buying_price, max_profit = prices[0], 0

        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - buying_price)
            buying_price = min(buying_price, prices[i])
        return max_profit


sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
print(sol.maxProfit([7,6,4,3,1]))
