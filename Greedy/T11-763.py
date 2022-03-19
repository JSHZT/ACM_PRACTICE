class Solution(object):
    def partitionLabels(self, s):
        lens = len(s)
        rec = [0] * lens
        right = 0
        for i in range(lens):
            rec[ord(s[i])-ord('a')] = i
        ans = []
        temp = 0
        for i in range(lens):
            right = max(right, rec[ord(s[i])-ord('a')])
            temp += 1
            if i == right:
                ans.append(temp)
                temp = 0
        return ans
        