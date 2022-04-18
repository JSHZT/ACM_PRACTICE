class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        strs = list(s)
        stack = []
        lens = len(s)
        for i in range(lens):
            while stack and stack[-1] >= strs[i] and strs[].count(stack[-1]) > 1:
                stack.pop()
            stack.append(strs[i])
        ans = ''.join(stack)
        return ans