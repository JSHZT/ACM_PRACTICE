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
