class Solution(object):
    def findContentChildren(self, g, s):
        leng = len(g)
        lens = len(s)
        if leng == 0 or lens == 0:
            return 0
        index = lens - 1
        ans = 0
        s.sort()
        g.sort()
        for i in range(leng-1, -1, -1):
            if s[index] >= g[i]:
                index -= 1
                ans += 1
            if index < 0:
                break
        return ans