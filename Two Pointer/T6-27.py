class Solution(object):
    def removeElement(self, nums, val):
        slow = fast = 0
        while fast < len(nums):
            if nums[slow] != val:
                slow += 1
                nums[slow]  = nums[fast]
            fast += 1
        return slow