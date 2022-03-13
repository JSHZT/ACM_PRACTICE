class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        lens1 = len(nums1)
        lens2 = len(nums2)
        dp = [[0 for _ in range(lens2+1)] for _ in range(lens1+1)]
        for i in range(1, lens1+1):
            for j in range(1, lens2+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]