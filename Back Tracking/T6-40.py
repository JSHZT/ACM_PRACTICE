class Solution(object):
    def combinationSum2(self, candidates, target):
        ans = []
        temp = []
        candidates.sort()
        lens = len(candidates)
        def backtracking(start_index, sum):
            if sum > target:
                return
            if sum == target:
                ans.append(temp[:])
                return
            for i in range(start_index, lens):
                if sum + candidates[i] > target:
                    return
                if i>start_index and candidates[i] == candidates[i-1]:
                    continue
                temp.append(candidates[i])
                backtracking(i+1, sum + candidates[i])
                temp.pop()
        backtracking(0, 0)
        return ans
    
if __name__ == '__main__':
    candidates = [10,1,2,7,6,1,5]
    target = 8
    ans = Solution().combinationSum2(candidates, target)