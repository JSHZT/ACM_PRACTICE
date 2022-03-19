class Solution(object):
    def countSubstrings(self, s):
        lens = len(s)
        if lens <= 1:
            return lens
        ans = 0
        dp = [[False for _ in range(lens+1)] for i in range(lens+1)]
        
        for i in range(lens+1, 0, -1):
            for j in range(1, lens+1):
                if s[i] == s[j]:
                    if i-j <= 1:
                        dp[i][j] = True
                        ans += 1
                    else:
                        if(dp[i+1][j-1]):
                            ans += 1
        return ans