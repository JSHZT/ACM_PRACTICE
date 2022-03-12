class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0 for j in range(target+1)]
        dp[0] = 1
        for j in range(target+1):
            for i in range(len(nums)):
                if(j-nums[i]>=0):
                    dp[j] += dp[j-nums[i]]
        return dp[-1]