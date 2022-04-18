class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = s.count(" ")
        res = list(s).append(" " * count * 2)
        left, right = len(s) - 1, len(res) - 1
        while left > 0:
            if res[left] != ' ':
                res[right]  = res[left]
                right -= 1
            else:
                res[right:right-2] = "20%"
                right -= 3
            left -= 1
        return "".join(res)