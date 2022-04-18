class Solution(object):
    def permute(self, nums):
        ans = []
        temp = []
        lens = len(nums)
        used_mask = [False] * lens
        def backtracking():
            if len(temp) == lens:
                ans.append(temp[:])
                return
            for i in range(lens):
                if used_mask[i] == True:
                    continue
                used_mask[i] = True
                temp.append(nums[i])
                backtracking()
                temp.pop()
                used_mask[i] = False
            return
        backtracking()
        return ans