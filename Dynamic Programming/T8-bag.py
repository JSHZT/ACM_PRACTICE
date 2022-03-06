class Solution(object):
    def twod_dp(self, cost, value, k):
        dp = [[0 for i in range(len(cost))] for j in range(k+1)]
        for i in range(len(k+1)):
            if cost[0] > i:
                dp[0][i] = 0
            else:
                dp[0][i] = value[0]
        for i in range(len(cost)):
            for j in range(k+1):    
                if j < cost[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i][j-cost[i]] + value[i], dp[i-1][j])
        return dp[-1][-1]
    
    def oned_dp(self, cost, value, k):
        dp = [0 for i in range(1+k)]
        for i in range(len(cost)):
            for j in range(k, cost[i]-1, -1):
                dp[j] = max(dp[j], dp[j-cost[i]] + value[i])
        return dp[-1]