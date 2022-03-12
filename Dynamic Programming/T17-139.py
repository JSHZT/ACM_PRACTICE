class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        lens = len(s)
        dp = [False for i in range(lens+1)]
        dp[0] = True
        for j in range(lens+1):
            for i in range(j+1): 
                if s[j-i:j] in wordDict and dp[j-i]:
                    dp[j] = True
        return dp[-1]
        