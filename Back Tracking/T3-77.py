class Solution(object):
    def combine(self, n, k):
        combination = []
        ans = []
        backtracking(n, 0, k)
    
        def backtracking(n, now, k):
            if len(combination) == k:
                ans.append(combination[:])
                return
            for j in range(now + 1, n + 1):
                combination.append(j)
                backtracking(n, j, k)
                combination.remove(j)
            return
