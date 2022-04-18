class Solution(object):
    def subsets(self, nums):
        ans = []
        temp = []
        lens = len(nums)
    
        def backtarcking(index):
            if temp not in ans:
                ans.append(temp[:])
            if index == lens:
                if temp[:] not in ans:
                    ans.append(temp[:])
                return
            for i in range(index, lens):
                temp.append(nums[i])
                backtarcking(i+1)
                temp.pop()
            return
        backtarcking(0)
        return ans