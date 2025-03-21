from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [None] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                if dp[i - coin] is None:
                    continue

                if dp[i]:
                    dp[i] = min(dp[i - coin] + 1, dp[i])
                else:
                    dp[i] = dp[i - coin] + 1

        return -1 if dp[amount] is None else dp[amount]

sol = Solution()
print(sol.coinChange([1, 2, 5], 11))
print(sol.coinChange([2], 3))
print(sol.coinChange([1], 0))
