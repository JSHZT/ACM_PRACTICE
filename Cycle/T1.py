class Solution(object):
    def convert(self, s, numRows):
        if numRows is 1:
            return s
        result = ['']*numRows
        n = (2*numRows-2)
        for i in range(len(s)):
            k = i%n
            result[min(k, n - k)] += s[i]
        return ''.join(result)