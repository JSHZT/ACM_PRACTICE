class Solution(object):
    def permuteUnique(self, nums):
        ans = []
        temp = []
        lens = len(nums)
        used_mask = [False] * lens
        nums.sort()
        def backtracking():
            if len(temp) == lens:
                ans.append(temp[:])
                return
            for i in range(lens):
                if used_mask[i] == True or (i > 0 and nums[i] == nums[i-1] and not used_mask[i-1]):
                    continue
                used_mask[i] = True
                temp.append(nums[i])
                backtracking()
                temp.pop()
                used_mask[i] = False
            return
        backtracking()
        return ans
    
nums = [1,1,2]
ans = Solution().permuteUnique(nums)