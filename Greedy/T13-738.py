class Solution(object):
    def monotoneIncreasingDigits(self, n):
        strnums = list(str(n))
        for i in range(len(strnums) - 1):
            if int(strnums[i])<int(strnums[i+1]):
                strnums[i]  = str(int(strnums[i]) - 1)
                strnums[i+1:] = '9'
        return (''.join(strnums))