class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lens = len(nums)
        dp = [1 for _ in range(lens)]
        for i in range(1, lens):
            if nums[i-1]<nums[i]:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = 1
        return max(dp) 