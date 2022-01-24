<a name="VIFqk"></a>
## 题目一：求最长不重复字符串
<a name="S0V5R"></a>
### 题目描述：
输入一个字符串，返回在字符串中的最长不重复的字符串长度
<a name="TfzNo"></a>
### 示例：
**输入: **s = "abcabcbb" <br />**输出: **3  <br />**解释:** 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
<a name="WBggN"></a>
### 解决思路：
使用一个空列表，依次在右边加入新元素，在左边弹出重复的元素，字符串长度在每一轮迭代更新的时候将当前长度跟上一次的长度做对比，选取最长的长度，依次执行，即可得解
<a name="DR7Dv"></a>
### 解决代码：
```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        cur = []
        ans = 0
        for i in range(len(s)):
            while s[i] in cur:
                cur.pop(0)
            cur.append(s[i])
            ans = max(len(cur), ans)
        return ans
```
