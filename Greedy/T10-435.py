class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        lens = len(intervals)
        if lens == 0:
            return 0
        intervals.sort(key = lambda x: x[1])
        sel = 1
        for i in range(1, lens):
            if intervals[i][0] >= intervals[i-1][1]:
                sel += 1
            else:
                intervals[i][1] = intervals[i-1][1]
        return lens - sel
          