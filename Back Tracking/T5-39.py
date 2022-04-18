class Solution(object):
    def combinationSum(self, candidates, target):
        lens = len(candidates)
        ans = []
        temp = []
        candidates.sort()
        def backtracking(index, target):
            if target <= 0 or index>=lens:
                return
            if target >= candidates[index]:
                if target == candidates[index]:
                    temp.append(candidates[index])
                    ans.append(temp[:])
                    temp.pop()
                    return
                else:
                    temp.append(candidates[index])
                    backtracking(index, target-candidates[index])
                    temp.pop()
                    backtracking(index + 1, target)
            return
        backtracking(0, target)
        return ans