import functools


class Solution(object):
    def largestNumber(self, nums):
        strs = map(str, nums)
        def cmp(x, y):
            if x+y < y+x:
                return -1
            elif x+y > y+x:
                return 1
            else:
                return 0
        strs = sorted(strs, key=functools.cmp_to_key(cmp), reverse=True)
        return str(int(''.join(strs)))