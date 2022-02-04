class Solution(object):
    def threeSum(self, nums):
        lens = len(nums)
        nums.sort()
        ans = []
        for first in range(lens):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            res = -nums[first]
            third = lens - 1
            for second in range(first + 1, lens):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                while second < third and nums[second] + nums[third] > res:
                    third -= 1
                if second == third:
                    break
                if nums[second] + nums[third] == res:
                    ans.append([nums[first], nums[second], nums[third]])
        return ans