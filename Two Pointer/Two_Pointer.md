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
<a name="FPeMB"></a>
## 题目二：三数之和
<a name="SUX2i"></a>
### 题目描述：
给你一个包含** n **个整数的数组 **nums**，判断 **nums** 中是否存在三个元素** a，b，c** ，使得 **a + b + c = 0** ？请你找出所有和为** 0 且不重复的三元组**。<br />注意：答案中不可以包含重复的三元组。
<a name="d6EHR"></a>
### 示例：
**输入**：nums = [-1,0,1,2,-1,-4]<br />**输出**：[[-1,-1,2],[-1,0,1]]<br />​

**输入**：nums = []<br />**输出**：[]<br />​

**输入**：nums = [0]<br />**输出**：[]
<a name="an4Mj"></a>
### 解题思路：
三数的和，可以将第一项，即最小项进行移项，转换成两数之和。将序列排序后，可利用双指针的方法进行双向扫描。这是大致方向。具体细节要注意不能有重复结果，因此统一采用第一项移项，而第二项即通过左指针扫描的项从第一项的下一个开始（second = first + 1）。第一第二项的扫描还需注意剔除重复的数字。第三项作为右指针扫描
<a name="n7cd9"></a>
### 代码如下：
```python
class Solution(object):
    def threeSum(self, nums):
        lens = len(nums)
        nums.sort()
        ans = []
        for first in range(lens):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            res = -nums[first]
            third = lens - 1
            for second in range(first + 1, lens):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                while second < third and nums[second] + nums[third] > res:
                    third -= 1
                if second == third:
                    break
                if nums[second] + nums[third] == res:
                    ans.append([nums[first], nums[second], nums[third]])
        return ans
```
<a name="K2cpH"></a>
## 题目二：最接近的三数之和
<a name="uebhY"></a>
### 题目描述：
给你一个长度为** n** 的整数数组** nums **和 一个目标值 **target**。请你从** nums **中选出三个整数，使它们的和与** target** 最接近。返回这三个数的和。假定每组输入只存在恰好一个解。
<a name="kDuNA"></a>
### 示例:
**输入**：nums = [-1,2,1,-4], target = 1<br />**输出**：2<br />**解释**：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。<br />​

**输入**：nums = [0,0,0], target = 1<br />**输出**：0
<a name="MDu0W"></a>
### 解题思路：
与上一道题类似，三数之和依旧可以用双指针的方法来枚举。定义一个best变量在扫描过程中更新当前最好的结果（important！！！）。扫描方式依旧是通过比较sum和target的大小进行，sum大则右指针左移，sum小则左指针左移，直到两指针相遇为止。
<a name="UOpMP"></a>
### 代码如下:
```python
class Solution(object):
    def threeSumClosest(self, nums, target):
        lens = len(nums)
        nums.sort()
        sum = 0
        best = 2**31 - 1
        for first in range(lens):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            third = lens - 1
            for second in range(first + 1, lens):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                while second < third:
                    sum = nums[first] + nums[second] + nums[third]
                    if abs(best - target) > abs(sum - target):
                        best = sum
                    if sum > target:
                        third_ = third - 1
                        while second < third_ and nums[third] == nums[third_]:
                            third_ -= 1
                        third = third_
                    elif sum < target:
                        second_ =second + 1
                        while second_ < third and nums[second] == nums[second_]:
                            second_ += 1
                        second = second_
                    else:
                        return sum
        return best
```
​<br />
<a name="czvaG"></a>
## 题目三：四数之和
<a name="WBF5I"></a>
### 题目描述：
给你一个由 n 个整数组成的数组 **nums** ，和一个目标值 **target **。请你找出并返回满足下述全部条件且不重复的四元组** [nums[a], nums[b], nums[c], nums[d]] **（若两个四元组元素一一对应，则认为两个四元组重复）：<br />0 <= a, b, c, d < n<br />a、b、c 和 d 互不相同<br />nums[a] + nums[b] + nums[c] + nums[d] == target<br />你可以按 任意顺序 返回答案 。
<a name="hLdsl"></a>
### 示例：
**输入**：nums = [1,0,-1,0,-2,2], target = 0<br />**输出**：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]<br />​

**输入**：nums = [2,2,2,2,2], target = 8<br />**输出**：[[2,2,2,2]]
<a name="DSSFq"></a>
### 解题思路：
相比于三数之和，区别在于左右指针是第三第四个数，而另外两个数需要在外层循环中枚举，其他不必多说。值得注意的是：可以进行一些剪枝操作（加上节约时间，不加答案也一样）<br />1.确定一个数时，前四个数相加大于target，那么可以直接判断往后再也没有答案，直接break<br />2,确定一个数时，如果第一个数和序列最后面三个数相加小于target时，直接枚举下一个第一个数，continue<br />3.确定两个数时，若前两个数和序列最后两个数相加小于target，则同理枚举下一个第二个数<br />4.确定两个数时，前四个数如果相加大于target，则break
<a name="FIDq9"></a>
### 代码如下:
```python
class Solution(object):
    def fourSum(self, nums, target):
        lens = len(nums)
        nums.sort()
        ans = []
        for i in range(lens-3):
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[lens-3] + nums[lens-2] + nums[lens-1] < target:
                continue
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, lens-2):
                if j > i and nums[j] == nums[j-1]:
                    continue
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[lens-2] + nums[lens-1] < target:
                    continue
                left, right = j + 1, lens - 1
                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        left += 1
                        while left <right and nums[right] == nums[right-1]:
                            right -= 1
                        right -= 1
                    elif sum > target:
                            right -= 1
                    elif sum < target:
                        left += 1
        return ans
```
<a name="KhCso"></a>
## 题目四：删除链表倒数第N个节点
<a name="ZPZAC"></a>
### 题目描述:
给你一个链表，删除链表的倒数第 n_ _个结点，并且返回链表的头结点。
<a name="BIwXY"></a>
### 解题思路：
同样是双指针，只是这边向同一个方向移动，右指针比左指针快n个节点，那么右指针扫描到最右边的时候，左指针对应的值即是链表倒数第n个数
<a name="QNlHu"></a>
### 代码如下:
```python
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        return dummy.next
```
