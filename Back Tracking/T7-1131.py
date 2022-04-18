class Solution(object):
    def partition(self, s):
        ans = []
        temp = []
        lens = len(s)
        def is_huiwen(s, start, end):
            l, r = start, end
            while l != r and l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True
        
        def backtracking(start_index):
            if start_index >= lens:
                ans.append(temp[:])
                return
            if start_index == lens-1:
                temp.append(s[start_index])
                ans.append(temp[:])
                temp.pop()
                return
            for i in range(start_index, lens):
                if is_huiwen(s, start_index, i):
                    temp.append(s[start_index:i+1])
                    backtracking(i+1)
                    temp.pop()
            return
        backtracking(0)
        return ans
    
s = "aab"
ans = Solution().partition(s)