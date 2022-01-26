class Solution(object):
    def longestPalindrome(self, s):
        lens = len(s)
        if lens is 1:
            return s
        start = 0
        maxlen = 1
        dp = [[0 for i in range(lens)] for j in range(lens)]
        for i in range(lens):
            dp[i][i] = 1
    
        for j in range(lens):
            for i in range(j):
                if s[j] != s[i]:
                    dp[i][j] = 0
                else:
                    if j - i < 3:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and j - i + 1 > maxlen:
                    maxlen = j - i + 1
                    start = i
        return s[start:start + maxlen]
s = input()
ret = Solution().longestPalindrome(s)
print(ret)
        