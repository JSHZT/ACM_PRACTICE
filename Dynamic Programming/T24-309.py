class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ##0:持有 1：刚卖出 2：冻结期 3：自由状态 
        lens = len(prices)
        dp = [[0 for _ in range(4)] for _ in range(lens)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        dp[0][2] = 0
        dp[0][3] = 0
        for i in range(1, lens):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i], dp[i-1][3]-prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = dp[i-1][1]
            dp[i][3] = max(dp[i-1][2], dp[i-1][3])
        return max(dp[lens-1][3], dp[lens-1][2], dp[lens-1][1])