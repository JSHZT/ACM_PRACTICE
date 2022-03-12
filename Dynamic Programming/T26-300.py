class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lens = len(nums)
        dp = [0 for _ in range(lens+1)]
        dp[1] = 1
        for i in range(2, lens+1):
            for j in range(1, i):
                if nums[j]<nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return dp[-1]