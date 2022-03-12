class Solution(object):
    def rob(self, nums):
        lens = len(nums)
        if lens==0:
            return 0
        if lens==1:
            return nums[0]
        ans1 = self.robrange(nums, 0, lens-2)
        ans2 = self.robrange(nums, 1, lens-1)
        return max(ans1, ans2)
    
    def robrange(self, nums, l, r):
        if l == r: return nums[l]
        dp = [0] * len(nums)
        dp[l] = nums[l]
        dp[l+1] = max(nums[l], nums[l+1])
        for i in range(l+2, r+1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[r]