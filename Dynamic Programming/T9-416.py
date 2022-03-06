class Solution(object):
    def canPartition(self, nums):
        temp = sum(nums)
        if temp%2!=0:
            return False
        sum_ = temp >> 1
        dp = [0 for i in range(sum_+1)]
        for i in range(len(nums)):
            for j in range(sum_, nums[i]-1, -1):
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
        if dp[-1] == sum_:
            return True
        else:
            return False
    
    
if __name__ == '__main__':
    nums = [1, 5, 11, 5]
    ans = Solution().canPartition(nums)
    print(ans)
    