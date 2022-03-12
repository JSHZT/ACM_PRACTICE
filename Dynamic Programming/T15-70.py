class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        m = 2
        for j in range(n+1):
            for i in range(1, m):
                if j - i >=0:
                    dp[j] += dp[j-i]
        return dp[-1]