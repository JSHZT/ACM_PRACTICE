class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        N = len(nums1) + len(nums2)
        if N % 2 is 0:
            a = self.find_elem(nums1, nums2, N/2)
            b = self.find_elem(nums1, nums2, N/2+1)
            result = (a + b)*0.5
        else:
            result = self.find_elem(nums1, nums2, N/2+1)
        return float(result)

    def find_elem(self, nums1, nums2, k):
        len1 = len(nums1)
        len2 = len(nums2)
        index1 = 0
        index2 = 0
        while True:
            if index1 is len1:     ##若越界，则返回序列2的第k小的数
                return nums2[index2 + k - 1]
            elif index2 is len2:   ##若越界，则返回序列1的第k小的数
                return nums1[index1 + k - 1]
            elif k is 1:
                return min(nums1[index1], nums2[index2])
            new_index1 = min(index1 + k/2, len1) - 1
            new_index2 = min(index2 + k/2, len2) - 1
            A = nums1[new_index1]
            B = nums2[new_index2]
            if A >= B:
                k -= (new_index2 - index2 + 1)
                index2 = new_index2 + 1
            else:
                k -= (new_index1 - index1 + 1)
                index1 = new_index1 + 1