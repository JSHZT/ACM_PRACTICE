import math
class Prime(object):
    def is_Prime(self, x):
        for i in range(2, int(math.sqrt(x)+1)):
            if(x % i) == 0:
                return False
        return True
    
    def getPrimeList_Eratosthenes(self, l, r):
        if(l > r):
            print('the left could not bigger than the right!')
            return   
        if(r < 2):
            return[]
        if(l < 2):
            l = 2
        ans = [True for i in range(r+1)]
        for j in range(2, round(math.sqrt(r)) + 1):
            if ans[j]:
                for i in range(j * j, r+1, j):
                    ans[i] = False
        return [i for i in range(l, r+1) if ans[i]]
    
    def getPrimeList_Euler(self, l, r):
        return
if __name__ == '__main__':
    prime_tool = Prime()
    primelist = prime_tool.getPrimeList_Eratosthenes(2, 2)
    print(primelist)