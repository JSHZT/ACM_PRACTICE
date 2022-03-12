class Solution(object):
    def findMaxForm(self, strs, m, n):
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for elem in strs:
            zero_nums = elem.count('0')
            one_nums = elem.count('1')
            if zero_nums>m or one_nums>n:
                break
            for i in range(m, zero_nums-1, -1):
                for j in range(n, one_nums-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zero_nums][j-one_nums] + 1)
        return dp[-1][-1]
                