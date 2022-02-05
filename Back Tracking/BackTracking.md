<a name="Oj8Ly"></a>
## 题目一：电话号码的数字组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。<br />给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/12592409/1644045823960-398638dc-3725-4cc4-9464-af87b0c54894.png#clientId=u0807a855-2360-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=376&id=ua4c4a095&margin=%5Bobject%20Object%5D&name=image.png&originHeight=376&originWidth=468&originalType=binary&ratio=1&rotation=0&showTitle=false&size=113286&status=done&style=none&taskId=u13875117-9a18-47a0-b61e-9eb0af540af&title=&width=468)
<a name="djDzq"></a>
### 示例：
**输入**：digits = "23"<br />**输出**：["ad","ae","af","bd","be","bf","cd","ce","cf"]<br />​

**输入**：digits = ""<br />**输出**：[]<br />​

**输入**：digits = "2"<br />**输出**：["a","b","c"]
<a name="tMtiT"></a>
### 解题思路：
排列组合问题，等价是搜索问题，将每一个符合长度要求的搜索结果输出，对每个数字，有对应先后选择对应字母的关系，因此用下图的树来表示，不必多说。<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/12592409/1644045885780-1dc2b7b4-a7ee-473b-9a19-1991c903138a.png#clientId=u0807a855-2360-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=299&id=u2cf1e6eb&margin=%5Bobject%20Object%5D&name=image.png&originHeight=299&originWidth=459&originalType=binary&ratio=1&rotation=0&showTitle=false&size=27825&status=done&style=none&taskId=u39193028-b9a5-4790-b730-238c003e581&title=&width=459)
<a name="pcYbL"></a>
### 代码如下：
```python
class Solution(object):
    def letterCombinations(self, digits):
        if digits == "":
            return []
        PhoneMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        lens = len(digits)
        Combination = []
        Combinations = []
        
        def backtrack(index):
            if index == lens:
                Combinations.append("".join(Combination))
            else:
                digit = digits[index]
                for word in PhoneMap[digit]:
                    Combination.append(word)
                    backtrack(index + 1)
                    Combination.pop()
            
        backtrack(0)
        return Combinations
```
