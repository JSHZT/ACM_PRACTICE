class Solution(object):
    def minCostClimbingStairs(self, cost):
        lens = len(cost)
        dp = [0] * lens
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, lens):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return min(dp[lens - 2], dp[lens - 1])
            