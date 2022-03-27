class Solution(object):
    def monotoneIncreasingDigits(self, n):
        strnums = list(str(n))
        for i in range(len(strnums) - 1, 0, -1):
            if int(strnums[i]) < int(strnums[i-1]):
                strnums[i-1]  = str(int(strnums[i-1]) - 1)
                strnums[i:] = '9' *  (len(strnums) - i)
        return int(''.join(strnums))