class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        nums = sorted(nums, key=abs, reverse=True)
        for i in range(len(nums)):
            if nums[i]<0 and k>0:
                nums[i] = -nums[i]
                k -= 1
        if k>0:
           if k%2 != 0:
               nums[-1] = -nums[-1]
        return sum(nums)
                