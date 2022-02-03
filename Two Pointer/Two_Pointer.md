<a name="pFBQ1"></a>
## 方法描述：
此方法为蛮力遍历的另一种优化，主要是利用指向一个序列的两个指针进行扫描，将空间复杂度和时间复杂度进行简化。
<a name="uf1qX"></a>
## 特征：
多用于一个序列需要用到两个值、扫描两边的情况，也能视情况而定，比如求未知长度的单链表的n分点或者整理奇偶序列，使序列左边是奇数，有边是偶数等。
<a name="Yv0Mh"></a>
## 题目一：盛最多水的容器
<a name="gB0lM"></a>
### 题目描述：
给你 n 个非负整数** a1，a2，...，an**，每个数代表坐标中的一个点** (i, ai)** 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为** (i, ai) **和** (i, 0)** 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
<a name="r4oXU"></a>
### 示例：
输入：**[1,8,6,2,5,4,8,3,7]**<br />输出：49 <br />解释：图中垂直线代表输入数组** [1,8,6,2,5,4,8,3,7]**。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/12592409/1643875742965-0dbcfdbf-efa0-4860-a099-5ada74632c43.png#clientId=u8d2185a1-72b5-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=380&id=uca66f369&margin=%5Bobject%20Object%5D&name=image.png&originHeight=380&originWidth=798&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24234&status=done&style=none&taskId=uf7161b18-9fe2-408e-a037-c71c7fd7e97&title=&width=798)
<a name="EIxN5"></a>
### 解题思路：
本题目实际上是求最大面积，最大面积主要受限于两点：<br />1.最短边<br />2.当两边相等的时候，离得越远越好<br />那么本题中便可利用双指针在头尾扫描，依次记录当前最大面积并移动较小边的指针，直到两指针相遇，则当前最大面积即为全局最大面积
<a name="d0w3u"></a>
### 代码如下：
```python
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
```
