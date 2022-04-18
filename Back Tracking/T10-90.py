class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        ans = []
        temp = []
        lens = len(nums)
        def backtracking(start_index):
            if temp[:] not in ans:
                ans.append(temp[:])
            if start_index >= lens:
                if temp[:] not in ans:
                    ans.append(temp[:])
                return
            for i in range(start_index, lens):
                if i> start_index and (nums[i] == nums[i-1]):
                    continue
                temp.append(nums[i])
                backtracking(i+1)
                temp.pop()
            return
        
        backtracking(0)
        return ans