class Solution(object):
    def integerBreak(self, n):
        dp = [0] * (n + 1)
        dp[0], dp[1] = 0, 0
        for i in range(2, n+1):
            for j in range(i):
                dp[i] = max(dp[i], j*(i - j), j*dp[i-j])
        return dp[-1]
    
if __name__ == '__main__':
    max_ = Solution().integerBreak(2)
    print(max_)