class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtrack(left, right):
            if left + right == 2 * n:
                Combinations.append("".join(Combination))
            if left<n:
                Combination.append("(")
                backtrack(left + 1, right)
                Combination.pop()
            if left>right:
                Combination.append(")")
                backtrack(left, right+1)
                Combination.pop()  
        
        Combination = []
        Combinations = []
        backtrack(0, 0)
        return Combinations
    
n = 1
Combinations = Solution().generateParenthesis(n)
print(Combinations)