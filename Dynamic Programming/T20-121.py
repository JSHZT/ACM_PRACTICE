class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [[0 for _ in range(len(prices))] for _ in range(2)]
        dp[0][0] = -prices[0]
        dp[1][0] = 0
        for i in range(1, len(prices)):
            dp[0][i] = max(dp[0][i-1], prices[i])
            dp[1][i] = max(dp[1][i-1], dp[0][i-1] + prices[i])
        return dp[1][-1]
            