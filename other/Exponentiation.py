class Exponentiation(object):
    def Recursion_to_do(self, a, x):
        if x == 0:
            return 1
        elif x & 1:
            return self.Recursion_to_do(a, x - 1) * a
        else:
            temp = self.Recursion_to_do(a, x >> 1)
            return temp * temp
    
    def NotRecursion_to_do(self, a, x):
        ans = 1
        while x != 0:
            if x & 1:
                ans *= a
            a *= a
            x = x >> 1
        return ans
