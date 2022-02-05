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

digits = ""
Combinations = Solution().letterCombinations(digits)
print(Combinations)