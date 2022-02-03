class Solution(object):
    def isMatch(self, s:str, p:str)->bool:
        lensP = len(p)
        lensS = len(s)
        dp = [[False for i in range(lensP+1)] for j in range(lensS+1)]
        dp[0][0] = True
        for i in range(1, lensP):
            if p[i-1] == '*':
                dp[i][0] = dp[i-2][0]
        for i in range(1, lensP + 1):
            for j in range(1, lensS + 1):
                if p[i-1] == '*':
                    if self.match(s[j-1], p[i - 2]):
                        dp[i][j] = dp[i-2][j] or dp[i][j-1]
                    else:
                        dp[i][j] = dp[i-2][j]
                else:
                    dp[i][j] = dp[i-1][j-1]
                        
        return dp[-1][-1]  

    def match(self, char1, char2):
        return char1 == char2 or char2 == '.'
 