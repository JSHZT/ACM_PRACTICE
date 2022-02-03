from socket import herror


class Solution(object):
    def maxArea(self, height):
        l = 1
        r = len(height)
        max_  = 0
        while l != r:
            max_ = max(min(height[r-1], height[l-1]) * ( r - l), max_)
            if height[l-1] < height[r-1]:
                l += 1
            else:
                r -= 1
        return max_ 


height = [1, 1]
max_ = Solution().maxArea(height)
print(max_)