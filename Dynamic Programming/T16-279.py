from math import sqrt

class Solution(object):
    def numSquares(self, n):
        dp = [2**31 for _ in range(n+1)]
        dp[0] = 0
        for i in range(int(math.sqrt(n)+1)):
            for j in range(i*i, n+1):
                dp[j] = min(dp[j-i*i]+1, dp[j])
        return dp[-1]
    

if __name__ == "__main__":
    ans = Solution().numSquares(12)
    print(ans)