class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        lens = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(lens)]
        dp[0][0] = -prices[0] - fee
        dp[0][1] = 0
        for i in range(1, lens):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - fee - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        return dp[lens-1][1]