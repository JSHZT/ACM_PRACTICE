class Solution(object):
    def numTrees(self, n):
        dp = [0]*(n+1)
        dp[1] = dp[0] = 1
        for i in range(2, n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-j-1]
        return dp[n]
if __name__ == '__main__':
    nums = Solution().numTrees(3)
    print(nums)