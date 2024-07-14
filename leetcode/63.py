from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0 for i in range(len(obstacleGrid[0]))] for i in range(len(obstacleGrid))]

        for i in range(len(obstacleGrid) - 1, -1, -1):
            if obstacleGrid[i][-1] == 1:
                break
            dp[i][-1] = 1
        for i in range(len(obstacleGrid[0]) - 1, -1, -1):
            if obstacleGrid[-1][i] == 1:
                break
            dp[-1][i] = 1


        for i in range(len(dp) - 2, -1, -1):
            for j in range(len(dp[0]) -2, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]

sol = Solution()
# print(sol.uniquePathsWithObstacles([[0,1,0], 
#                                     [0,0,0],
#                                     [0,0,0]]))

print(sol.uniquePathsWithObstacles([[0, 1], [0, 0]]))
