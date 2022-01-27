<a name="ZVzEI"></a>
## 特征：
有多个、有限个状态，需要根据不同的状态、不同的是输入来确定下一个状态，进行不同的工作<br />​<br />
<a name="KgDjS"></a>
## 题目一：字符转换整数
<a name="wlBid"></a>
### 题目描述:
给定一个字符串,包含空格和'+''-'以及数字部分,设计一个算法,将字符串转换成整数输出.<br />

<a name="EEqlg"></a>
### 示例:
**输入：**s = "42" <br />**输出：**42<br />**​**

**输入：**s = "   -42"<br />**输出：**-42
<a name="cYkId"></a>
### 解题思路:
转换过程有三个步骤,首先将前导空格删除,其次判断正负,最后读取数字,而针对三种情况的不同输入,可以列出下方的表格:<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/12592409/1643276625029-9437553b-cab9-4586-b23c-c8bdde59f064.png#clientId=u36721cb8-8e14-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=200&id=ud33a0a88&margin=%5Bobject%20Object%5D&name=image.png&originHeight=250&originWidth=954&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24382&status=done&style=none&taskId=uf92b80c6-a8d1-4d89-996b-51b165638c0&title=&width=763.2)<br />因此,采用有限状态机的方法解决此道问题
<a name="MCCiB"></a>
### 代码如下:
```python
INT_MAX = 2 ** 31 -1 #整数范围
INT_MIN = -2 ** 31


class Solution(object):
    def myAtoi(self, s):
        ret = StateMachine()
        for i in s:
            ret.get(i)
        return ret.signed * ret.ans
    

class StateMachine():
    def __init__(self):
        self.ans = 0
        self.signed = 1
        self.state = 'start'
        self.state_set = {
            'start':['start', 'signed', 'in_number', 'end'],
            'signed':['end', 'end', 'in_number', 'end'],
            'in_number':['end', 'end', 'in_number', 'end'],
            'end':['end', 'end', 'end', 'end']
        }
    
    def get_col(self, char):
        if char.isspace():
            return 0
        if char == '+' or char == '-':
            return 1
        if char.isdigit():
            return 2
        return 3
    
    def get(self, char):
        self.state = self.state_set[self.state][self.get_col(char)]
        if self.state is 'signed':
            self.signed = -1 if char == '-' else 1
        elif self.state is 'in_number':
            self.ans = self.ans * 10 + int(char)
            self.ans = min(self.ans, -INT_MIN) if self.signed is -1 else min(self.ans, INT_MAX)
```
