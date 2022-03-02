import math
class Prime(object):
    def is_Prime(self, x):
        for i in range(2, int(math.sqrt(x)+1)):
            if(x % i) == 0:
                return False
        return True
    
    def getPrimeList_Eratosthenes(self, l, r):
        ans = [True for i in range(r+1)]
        for j in range(2, round(math.sqrt(r)) + 1):
            if ans[j]:
                for i in range(j * j, r+1, j):
                    ans[i] = False
        return [i for i in range(l, r+1) if ans[i]]
    
    def getFactorsList(self, l, n):
        temp = ''
        while n>1:
            for i in l:
                if n % i == 0:
                    n = n / i
                    if n != 1:
                        temp += str(i) + '*' 
                    else:
                        temp += str(i) 
                    break
        return temp
            
if __name__ == '__main__':
    prime_tool = Prime()
    while True:
        try:
            num_in = list(map(int, input().split()))
            nums = [i for i in range(num_in[0], num_in[1]+1)]
            l = 2
            r = max(nums)
            PrimeList = prime_tool.getPrimeList_Eratosthenes(l, r)
            for num in nums:
                ans = str(num) + '=' + prime_tool.getFactorsList(PrimeList, num)
                print(ans)
        except:
            break