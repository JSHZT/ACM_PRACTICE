class Solution(object):
    def restoreIpAddresses(self, s):
        ans = []
        path = []
        lens = len(s)
        def is_ok(s, start, i):
            temp = s[start:i+1]
            if int(temp) > 255 or (temp[0] == '0' and len(temp) != 1):
                return False
            return True
        
        def backtracking(start_index):
            if len(path) > 4:
                return
            if start_index >= lens:
                if len(path) == 4:
                    temp = str(path[0])
                    for i in range(1, 4):
                        temp += "." + str(path[i])
                    ans.append(temp)
                return
            for i in range(start_index, lens):
                if len(path) >= 4:
                    return
                if is_ok(s, start_index, i):
                    path.append(s[start_index:i+1])
                    backtracking(i+1)
                    path.pop()
            return
        backtracking(0)
        return ans
    
if __name__ == '__main__':
    s = "101010"
    ans = Solution().restoreIpAddresses(s)