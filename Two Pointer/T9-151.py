class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s.strip(" ")
        res = list(s)
        lens = len(res)
        left, right = 0, 0
        while right < lens: 
            if res[right] != ' ' and right + 1 < lens:
                right += 1
            elif res[right] == ' ':
                res[left:right] = res[right-1:left-1]
                while right == ' ':
                    right += 1
                left = right
            elif right + 1 >= lens:
                res[left:right+1] = res[right:left]
                while right == ' ':
                    right += 1
                left = right
        return "".join(res)
s = "the sky is blue"    
res = Solution().reverseWords(s)