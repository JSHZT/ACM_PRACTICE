class Solution(object):
    def findSubsequences(self, nums):
        ans = []
        temp = []
        lens = len(nums)
        def backtracking(start_index):
            if len(temp) >= 2:
                ans.append(temp[:])
            used_list = set()
            for i in range(start_index, lens):
                if (temp and nums[i] < temp[-1]) or nums[i]  in used_list:
                    continue
                temp.append(nums[i])
                backtracking(i+1)
                temp.pop()
                used_list.add(nums[i])
                
            return
        backtracking(0)
        return ans
