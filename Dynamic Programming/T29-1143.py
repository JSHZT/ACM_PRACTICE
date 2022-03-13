class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        lens1 = len(text1)
        lens2 = len(text2)
        dp = [[0 for _ in range(lens1+1)] for _ in range(lens2+1)]
        for i in range(1, lens2+1):
            for j in range(1, lens1+1):
                if text1[j-1] == text2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]