class Solution(object):
    def maxProfit(self, k, prices):
        lens = len(prices)
        if lens==0:
            return 0
        temp = 2 * k + 1
        dp = [[0 for _ in range(temp)] for _ in range(lens)]
        for i in range(1, temp-1, 2):
            dp[0][i] = -prices[0]
        for i in range(1, lens):
            dp[i][0] = dp[i-1][0]
            for state in range(0, temp-2, 2):
                dp[i][state+1] = max(dp[i-1][state+1], dp[i][state]-prices[i])
                dp[i][state+2] = max(dp[i-1][state+2], dp[i][state+1]+prices[i])
        return dp[-1][temp - 1]