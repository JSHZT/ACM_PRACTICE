class Solution(object):
    def findTargetSumWays(self, nums, target):
        temp = sum(nums)
        if temp < abs(target) or (temp+target) % 2 != 0:
            return 0
        sum_ = (temp + target) >> 1
        dp = [0 for _ in range(sum_ + 1)]
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(sum_, nums[i]-1, -1):
                dp[j] += dp[j-nums[i]]
        return dp[-1]
    
nums = [100]
target = -200
ans = Solution().findTargetSumWays(nums, target)
print(ans)