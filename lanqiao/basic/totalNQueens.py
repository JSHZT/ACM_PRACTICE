class Solution(object):
    def totalNQueens(self, n, s):
        temp_w = [None for i in range(n)]
        temp_b = [None for i in range(n)]
        
        ans = []
        
        self.dfs_w(temp_w, temp_b, 0, ans, n, s)
        return len(ans)
    
    def dfs_w(self, temp_w, temp_b, row, ans, n, s):
        if row == n:
            self.dfs_b(temp_b, temp_w, 0, ans, n, s)
        else:
            for col in range(n):
                temp_w[row] = col
                if self.valid_w(temp_w, row, s):
                    self.dfs_w(temp_w, temp_b, row+1, ans, n, s)
        return
    
    def dfs_b(self, temp_b, temp_w, row, ans, n, s):
        if row == n:
            ans.append(temp_b[:])
            return
        else:
            for col in range(n):
                temp_b[row] = col
                if self.valid_b(temp_b, temp_w, row, s):
                    self.dfs_b(temp_b, temp_w, row+1, ans, n, s)
        return
        
    def valid_w(self, temp_w, row, s):
        if s[row][temp_w[row]] == '1':
            for i in range(row):
                if abs(temp_w[row] == temp_w[i]) or (abs(i-row) == abs(temp_w[i] - temp_w[row])):
                    return False
            return True
        return False
    
    def valid_b(self, temp_b, temp_w, row, s):
        if s[row][temp_b[row]] == '1' and temp_w[row] != temp_b[row]:
            for i in range(row):
                if abs(temp_b[row] == temp_b[i]) or (abs(i-row) == abs(temp_b[i] - temp_b[row])):
                    return False
            return True
        return False
    
    
if __name__ == '__main__':
    nums = 4
    s = [
        ['1', '1', '1' , '1'],
        ['1', '1', '1' , '1'],
        ['1', '1', '1' , '1'],
        ['1', '1', '1' , '1']
    ]
    solution = Solution().totalNQueens(nums, s)
    print(solution)
