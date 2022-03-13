class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lens = len(s)
        lent = len(t)
        dp = [[0 for _ in range(lent+1)] for _ in range(lens+1)]
        for i in range(1, lens+1):
            for j in range(1, lent+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i][j-1]
        if lens == dp[-1][-1]:
            return True
        return False