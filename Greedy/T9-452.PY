class Solution(object):
    def findMinArrowShots(self, points):
        nums_p = len(points)
        if nums_p <= 1:
            return nums_p
        points.sort(key = lambda x: x[0])
        ans = 1
        for i in range(1, nums_p):
            if points[i][0] > points[i-1][1]:
                ans += 1
            else:
                points[i][1] = min(points[i][1], points[i-1][1])
        return ans