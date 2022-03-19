class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lens = len(nums)
        if lens <= 1:
            return lens
        cur_distance = 0
        next_distance = 0
        ans = 0
        for i in range(lens):
            next_distance = max(i+nums[i], next_distance)
            if(i==cur_distance):
                cur_distance = next_distance
                ans += 1
                if cur_distance >= lens-1: 
                    break
        return ans