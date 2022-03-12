class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        len1 = len(nums1)
        len2 = len(nums2)
        ans = 0
        dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
            ans = max(ans, dp[i][j])
        return ans