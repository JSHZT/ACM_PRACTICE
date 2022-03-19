class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        range = 0
        lens = len(nums)
        index = 0
        while index <= range:
            range = max(index + nums[index], range)
            if range >= lens:
                return True
        return False