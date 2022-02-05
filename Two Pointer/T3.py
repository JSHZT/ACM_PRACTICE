class Solution(object):
    def threeSumClosest(self, nums, target):
        lens = len(nums)
        nums.sort()
        sum = 0
        best = 2**31 - 1
        for first in range(lens):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            third = lens - 1
            for second in range(first + 1, lens):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                while second < third:
                    sum = nums[first] + nums[second] + nums[third]
                    if abs(best - target) > abs(sum - target):
                        best = sum
                    if sum > target:
                        third_ = third - 1
                        while second < third_ and nums[third] == nums[third_]:
                            third_ -= 1
                        third = third_
                    elif sum < target:
                        second_ =second + 1
                        while second_ < third and nums[second] == nums[second_]:
                            second_ += 1
                        second = second_
                    else:
                        return sum
        return best

nums = [-1, 2, 1, 4]
best = Solution().threeSumClosest(nums, 1)
print(best)