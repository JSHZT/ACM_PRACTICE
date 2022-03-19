class Solution(object):
    def merge(self, intervals):
        
        lens = len(intervals)
        intervals.sort(key = lambda x: x[0])
        temp_start = intervals[0][0]
        temp_end = intervals[0][1]
        ans = []
        for i in range(1, lens):
            if intervals[i][0] <= intervals[i-1][1] :
                if intervals[i][1] <= intervals[i-1][1]:
                    temp_end = intervals[i][1]
                else:
                    intervals[i] = intervals[i-1]
            elif intervals[i][0] > intervals[i-1][1]:
                ans.append([temp_start, temp_end])
                temp_start = intervals[i][0]
                temp_end = intervals[i][1]
        ans.append([temp_start, temp_end])
            
        return ans
            