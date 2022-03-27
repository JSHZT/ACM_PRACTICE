class Solution(object):

    def fizz_buzz(self, num):
        if num is None:
            raise TypeError
        elif num < 1:
            raise ValueError
        ans = [''] * num
        for i in range(1, num+1):
            if i % 3 == 0:
                if i % 5 == 0:
                    ans[i-1] = 'FizzBuzz'        
                else:
                    ans[i-1] = 'Fizz'
            elif i % 5 == 0:
                ans[i-1] = 'Buzz'        
            else:
                ans[i-1] = str(i)      
        return ans