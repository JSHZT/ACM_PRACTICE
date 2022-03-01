class Solution(object):
    def compute_An(self, n):
        An = ''
        i = 1
        while i < n:
            if i & 1:
                An += ('sin(' + str(i) + '-')
            else:
                An += ('sin(' + str(i) + '+')
            i += 1
        An += ('sin(' + str(i))
        i = 0
        An += ')' * n
        return An

    
    def compute_Sn(self, n):
        i = 1
        Sn = ''
        Sn += '(' * (n-1)
        while n >= 1:
            Sn += self.compute_An(i) + '+' + str(n)
            if n != 1:
                Sn += ')'
            n -= 1
            i += 1
        return Sn
    