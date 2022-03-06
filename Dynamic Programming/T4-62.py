class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[1 for j in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n): 
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[-1][-1]
        
        
if __name__ == '__main__':
    paths = Solution().uniquePaths(3, 7)
    print(paths)