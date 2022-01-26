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
​<br />
