class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1 = len(word1)
        len2 = len(word2)
        dp = [[0 for _ in range(len1+1)] for _ in range(len2+1)]
        for i in range(len1+1):
            dp[0][i] = i
        for j in range(len2+1):
            dp[j][0] = j
        for j in range(1, len1+1):
            for i in range(1, len2+1):
                if word1[j-1] != word2[i-1]:
                    dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + 2)
                else:
                    dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]