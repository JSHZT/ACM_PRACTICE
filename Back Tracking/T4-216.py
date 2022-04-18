class Solution(object):
    def combinationSum3(self, k, n):
        if k > 9 or n <= 0:
            return []
        ans = []
        path = []
        def backtracking(start):
            if len(path) == k:
                if sum(path) == n:
                    ans.append(path[:])  
                return
            for i in range(start+1, 10):
                path.append(i)
                backtracking(i)
                path.pop()
            return
        backtracking(0)
        return ans
