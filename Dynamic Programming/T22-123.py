class Solution(object):
    def maxProfit(self, prices):
        #0:不操作 1：第一次买入 2：第一次卖出 3：第二次买入 4：第二次卖出
        lens = len(prices)
        dp = [[0 for _ in range(5)] for _ in range(lens)]
        dp[0][1] = -prices[0]
        dp[0][3] = -prices[0]
        for i in range(1, lens):
            dp[i][0] = dp[i-1][0]
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            dp[i][2] = max(dp[i-1][1] + prices[i], dp[i-1][2])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
            dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])
        return dp[lens-1][4]