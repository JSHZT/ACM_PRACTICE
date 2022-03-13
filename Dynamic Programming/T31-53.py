class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lens =len(nums)
        dp = [0 for _ in range(lens)]
        for i in range(lens):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
        return dp[-1]