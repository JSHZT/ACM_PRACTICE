<a name="BAV2Z"></a>
## 特征：
能够进行**状态转移**，属于蛮力法的优化方法
<a name="QhtZ0"></a>
## 题目一：寻找最长的回文字符串
<a name="rov8A"></a>
### 题目描述：
给你一个字符串 s，找到 s 中最长的回文子串。
<a name="Pn9hC"></a>
### 示例：
**输入：**s = "babad"<br />**输出：**"bab"<br />**解释：**"aba也满足题意，题目只需要输出一个即可"<br />​<br />
<a name="jHBec"></a>
### 解题思路：
字符串类的题目需要用到枚举的思想，一个个地寻找符合题意的字符串。暴力枚举的优化改进便是动态规划，并且很明显，回文字符串就具有**状态转移**的性质。例如：“babab”是回文字符串，即使去掉首尾，中间的“aba”依旧是回文字符串（这里中间的长度严格大于2）。<br />**定义dp[i][j]为i到j这段字符是否为回文字符串**<br />**抽象得状态转移方程：s[i] == s[j] and dp[i+1][j-1]**<br />再除去特殊状态len(s)=1,直接返回原字符串，则可得以下代码：
<a name="iswQ1"></a>
### 代码如下：
```python
class Solution(object):
    def longestPalindrome(self, s):
        lens = len(s)
        if lens is 1:
            return s
        start = 0
        maxlen = 1
        dp = [[0 for i in range(lens)] for j in range(lens)]
        for i in range(lens):
            dp[i][i] = 1
    
        for j in range(lens):
            for i in range(j):
                if s[j] != s[i]:
                    dp[i][j] = 0
                else:
                    if j - i < 3:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and j - i + 1 > maxlen:
                    maxlen = j - i + 1
                    start = i
        return s[start:start + maxlen]
s = input()
ret = Solution().longestPalindrome(s)
print(ret)
```
<a name="nLFEl"></a>
## 题目二：正则表达式匹配
<a name="L9Iim"></a>
### 题目描述:
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。<br />**'.' **匹配任意单个字符<br />**'*' **匹配零个或多个前面的那一个元素<br />所谓匹配，是要**涵盖整个字符串**s的，而不是部分字符串。
<a name="AvXoK"></a>
### 示例：
**输入：**s = "aa" p = "a" <br />**输出：**false <br />**解释：**"a" 无法匹配 "aa" 整个字符串。<br />​

**输入**：s = "aa" p = "a*"<br />**输出**：true<br />**解释**：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。<br />​

**输入：**s = "ab" p = ".*" <br />**输出：**true <br />**解释：**".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。<br />​<br />
<a name="GJ28c"></a>
### 解题思路:
匹配字符串的条件实际上是第n位能够匹配，并且前n-1位也能匹配。除开蛮力解法，还能够利用状态转移的规律，填写状态转移表，利用动态规划降低时间复杂度。可以定义dp[i][j]为p的前i位和s的前j位能够匹配。<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/12592409/1643900035868-41236955-f88b-4daa-95cc-a9d16a60ce4b.png#clientId=u99895578-1735-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=574&id=u62309491&margin=%5Bobject%20Object%5D&name=image.png&originHeight=707&originWidth=762&originalType=binary&ratio=1&rotation=0&showTitle=false&size=41026&status=done&style=none&taskId=u21a865b4-0bba-4cac-8f8e-4c42571c371&title=&width=619)![image.png](https://cdn.nlark.com/yuque/0/2022/png/12592409/1643900091305-1ee5aa09-cd44-4c57-b717-445239cd96b5.png#clientId=u99895578-1735-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=580&id=u3cb54ff3&margin=%5Bobject%20Object%5D&name=image.png&originHeight=708&originWidth=756&originalType=binary&ratio=1&rotation=0&showTitle=false&size=63655&status=done&style=none&taskId=u1cb95e79-c400-433b-b58d-1df47bac02a&title=&width=619)<br />最后一个结果便是能否匹配的结果
<a name="M3oWj"></a>
### 代码如下：
```python
class Solution(object):
    def isMatch(self, s:str, p:str)->bool:
        lensP = len(p)
        lensS = len(s)
        dp = [[False for i in range(lensP+1)] for j in range(lensS+1)]
        dp[0][0] = True
        for i in range(1, lensP):
            if p[i-1] == '*':
                dp[i][0] = dp[i-2][0]
        for i in range(1, lensP + 1):
            for j in range(1, lensS + 1):
                if p[i-1] == '*':
                    if self.match(s[j-1], p[i - 2]):
                        dp[i][j] = dp[i-2][j] or dp[i][j-1]
                    else:
                        dp[i][j] = dp[i-2][j]
                else:
                    dp[i][j] = dp[i-1][j-1]
                        
        return dp[-1][-1]  

    def match(self, char1, char2):
        return char1 == char2 or char2 == '.'
 
```
<a name="LNVz4"></a>
## 题目三：爬楼梯 leetcode746
<a name="QB05k"></a>
### 题目描述:
给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。<br />请你计算并返回达到楼梯顶部的最低花费。
<a name="EPouT"></a>
### 示例:
输入：cost = [1,100,1,1,1,100,1,1,100,1]<br />输出：6<br />解释：你将从下标为 0 的台阶开始。<br />- 支付 1 ，向上爬两个台阶，到达下标为 2 的台阶。<br />- 支付 1 ，向上爬两个台阶，到达下标为 4 的台阶。<br />- 支付 1 ，向上爬两个台阶，到达下标为 6 的台阶。<br />- 支付 1 ，向上爬一个台阶，到达下标为 7 的台阶。<br />- 支付 1 ，向上爬两个台阶，到达下标为 9 的台阶。<br />- 支付 1 ，向上爬一个台阶，到达楼梯顶部。<br />总花费为 6 。
<a name="OLPx3"></a>
### 解题思路:
先从爬楼梯的方法种类考虑，对爬上第i层楼梯，可以由第i-1层爬一步或由第i-2层爬两步到达。选择哪种方式则需要判断哪一种的方法代价小，计算代价的时候又会考虑到第i-1层和第i-2层如何到达，选择方式同样是考虑代价最小，以此类推，到这里，解决思路已经比较清晰了。<br />定义dp[i]为到达第i层所需要的代价，则状态转移方程：dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])，值得留意一个细节，这里是先在当前台阶，付出当前台阶移动的代价，再移动，因此，转移之前，还需要加上代价。这里为了方便，稍作改进，dp[i]是到达当前阶梯所需要的代价，并且已经付出代价，做好跳到下一个阶梯的准备。<br />改进之后的递推式：dp[i] = min(dp[i-1], dp[i-2]) + cost[i]，这样的改进，则0和1的初始化就直接使用cost[0]和cost[1]。
<a name="PkWqu"></a>
### 代码如下：
```python
class Solution(object):
    def minCostClimbingStairs(self, cost):
        lens = len(cost)
        dp = [0] * lens
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, lens):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return min(dp[lens - 2], dp[lens - 1])
 
```
<a name="XoYxd"></a>
## 题目四：不同路径 Leetcode62
<a name="l253O"></a>
### 题目描述:
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。<br />机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。<br />问总共有多少条不同的路径？<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/12592409/1646487770737-edf184ec-2e33-442f-b378-4da90f1c3a96.png#clientId=u502c7ba6-ffc8-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=253&id=u5cc01f5b&margin=%5Bobject%20Object%5D&name=image.png&originHeight=283&originWidth=613&originalType=binary&ratio=1&rotation=0&showTitle=false&size=22909&status=done&style=none&taskId=u480774ad-361f-4f3c-8647-c54152f06cc&title=&width=548.3999938964844)
<a name="BGO0L"></a>
### 示例:
输入：m = 3, n = 2<br />输出：3<br />解释：<br />从左上角开始，总共有 3 条路径可以到达右下角。<br />1. 向右 -> 向下 -> 向下<br />2. 向下 -> 向下 -> 向右<br />3. 向下 -> 向右 -> 向下
<a name="JDYgV"></a>
### 解题思路:
先考虑到达某一个格子所能有的方法，只能是从上面的和左边的相邻的格子走一步过来，那么方法种数转换成了计算到达左边格子的方法和到达上边格子的方法，假设dp[i][j]是走到第i行第j列的格子的方法个数，得出状态转移方程：dp[i][j] = dp[i-1][j] + dp[i][j-1]  与斐波那契数列相同
<a name="YhFrB"></a>
### 代码如下:
```python
class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[1 for j in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n): 
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[-1][-1]
```
<a name="x0UkZ"></a>
## 题目五：不同路径Ⅱ leetcode63
<a name="PI2x4"></a>
### 题目描述:
题意与上一题相同，但本题考虑障碍物，将会给出一个矩阵，矩阵中有1的坐标代表障碍物，不能通过
<a name="X3gDx"></a>
### 解题思路:
当左边或上边格子是障碍物时，意味着不能算障碍物的这个格子，因此直接考虑逢障碍物置0的操作，然后依旧采用上一题的状态转移方程。而注意一个细节是边缘部分,上一题的代码是默认初始化为1，很明显，如果边缘存在障碍物，那么往后的边缘部分也一定是无法达到的，因此下面的代码在规划前，要先对边缘部分做好初始化。
<a name="VP52z"></a>
### 代码如下:
```python
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            dp[0][0] = 1
        for i in range(1, m):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = dp[i-1][0]
        for j in range(1, n):
            if obstacleGrid[0][j] != 1:
                dp[0][j] = dp[0][j-1]
        for i in range(1, m):
            for j in range(1, n):
                if(obstacleGrid[i][j]==1):
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1] 
```
<a name="Ojwa4"></a>
## 题目六:拆分整数leetcode343
<a name="qsM0K"></a>
### 题目描述:
给定一个正整数 n ，将其拆分为 k 个 **正整数** 的和（ k >= 2 ），并使这些整数的乘积最大化。<br />返回 你可以获得的最大乘积 。
<a name="zXdoD"></a>
### 示例：
输入: n = 2<br />输出: 1<br />解释: 2 = 1 + 1, 1 × 1 = 1<br />​

输入: n = 10<br />输出: 36<br />解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
<a name="w67xy"></a>
### 解题思路：
这里不要被题目带偏，觉得分2个数和三个数这样讨论情况，题目要求输出的是乘积最大值。定义dp[i]为正整数i能够得到的最大乘积，这个乘积由多少项得来的并不重要，因为既然能够这样表示，那么表示多项的时候就可以利用这个形式去搜索。仅考虑 j 和 i-j之间的问题即可。j和i-j直接相加即可满足相加为i的题意，为了满足乘积最大，需要对多项进行搜索，处理如下：对j，从1开始遍历，另一项用来拆，即转换成i-j的拆分问题，于是又状态转移方程: dp[i] = max(dp[i], j * dp[i-j], i *(i-j))
<a name="qxd6J"></a>
### 代码如下:
```python
class Solution(object):
    def integerBreak(self, n):
        dp = [0] * (n + 1)
        dp[0], dp[1] = 0, 0
        for i in range(2, n+1):
            for j in range(i):
                dp[i] = max(dp[i], j*(i - j), j*dp[i-j])
        return dp[-1]
```
<a name="DiKNS"></a>
## 题目七:不同的二叉搜索树 leetcode96
<a name="KfQKE"></a>
### 题目描述:
给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 **二叉搜索树** 有多少种？返回满足题意的二叉搜索树的种数。
<a name="RpWm0"></a>
### 示例:
**输入：**n = 3 <br />**输出：**5<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/12592409/1646490993665-2c59d9b9-d0cc-42e8-8be4-8a3e62cce6d1.png#clientId=u502c7ba6-ffc8-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=177&id=ueb523a0b&margin=%5Bobject%20Object%5D&name=image.png&originHeight=221&originWidth=899&originalType=binary&ratio=1&rotation=0&showTitle=false&size=85423&status=done&style=none&taskId=u2f0db10a-023e-4147-8255-a8b705285e2&title=&width=719.2)
<a name="tt7XP"></a>
### 解题思路：
题目仅要求给出数量，并没有要求列出每个树的样子，因此可以通过以不同的节点作头节点来搜索。当选好一个头节点时，剩下n-1个节点，左右依次遍历分配搜索。左右子树的种类数目相乘，即能得到n个节点的数量(计数原理)定义dp[i]为以i个节点构造树的数量<br />则状态更新需要遍历计算，详情见代码
<a name="Iid7i"></a>
### 代码如下:
```python
class Solution(object):
    def numTrees(self, n):
        dp = [0]*(n+1)
        dp[1] = dp[0] = 1
        for i in range(2, n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-j-1]
        return dp[n]
```
