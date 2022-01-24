<a name="BAV2Z"></a>
## 特征：
题目有要求**时间复杂度是log**的查找；题目**给定的序列有序；**
<a name="QhtZ0"></a>
## 题目一：寻找两个正序数组的中位数
<a name="rov8A"></a>
### 题目描述：
给定两个大小分别为**m**和**n**的**正序**（从小到大）数组**nums1**和**nums2**。请你找出并返回这两个正序数组的中位数。要求算法的时间复杂度为**O(log(m+n))**。
<a name="Pn9hC"></a>
### 示例：
**输入：**nums1 = [1,3], nums2 = [2] <br />**输出：**2.00000 <br />**解释：**合并数组 = [1,2,3] ，中位数 2<br />​

**输入**：nums1 = [1,2], nums2 = [3,4]<br />**输出**：2.50000<br />**解释**：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5<br />​

**输入：**nums1 = [], nums2 = [1] <br />**输出：**1.00000<br />​<br />
<a name="jHBec"></a>
### 解题思路：
①首先注意到是查找类型的题目、给定的数据是有序的、时间复杂度要求是log级别，处处指引着二分搜索的方向解决<br />②其次，便是问题分析，据常识而言，中位数的取值有两种情况，分别为序列元素数量为奇数和偶数两种情况：<br />奇数情况：中位数为中间的数，第**N/2+1**个<br />偶数情况：中位数为第**N/2**个与第**N/2+1**个和的一半<br />那么问题就转换成了分两种情况寻找整个序列的第**N/2**个小或第**N/2+1**个小的数，统称为**寻找第K小的数**<br />**③寻找第k小的数**这种问题有很多种方法，比如著名的堆排序，构造小顶堆、蛮力遍历等等。考虑到时间复杂度的约束以及有序序列，最优解是二分查找。这里稍微变形，二分的标志从范围由大到小转换成k值从大变到1，过程是每次除2。<br />**当两个序列的第K/2-1项比较时，必定能排除其中一个序列的前面的元素**
<a name="iswQ1"></a>
### 代码如下：
```python
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
```
​<br />
