class Solution(object):
    def fourSum(self, nums, target):
        lens = len(nums)
        nums.sort()
        ans = []
        for i in range(lens-3):
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[lens-3] + nums[lens-2] + nums[lens-1] < target:
                continue
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, lens-2):
                if j > i and nums[j] == nums[j-1]:
                    continue
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[lens-2] + nums[lens-1] < target:
                    continue
                left, right = j + 1, lens - 1
                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        left += 1
                        while left <right and nums[right] == nums[right-1]:
                            right -= 1
                        right -= 1
                    elif sum > target:
                            right -= 1
                    elif sum < target:
                        left += 1
        return ans
    
nums = [1,0,-1,0,-2,2]
target = 0
ans = Solution().fourSum(nums, target)
print(ans)
                