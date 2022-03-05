class HighAccuracyAlgorithm(object):
    def __add__(self, a, b):
        c = list(map(lambda x : 0, ('0' + a.strip() + b.strip())))
        a = list(map(lambda x: int(x), a.strip()))
        b = list(map(lambda x: int(x), b.strip()))
        while len(a)>len(b):
            b.insert(0, 0)
        while len(b)<len(a):
            a.insert(0, 0)
        start_index = len(c) - 1
        pos = 0
        for i in range(len(a) - 1, -1, -1):
            temp = a[i] + b[i] + c[start_index - pos]
            c[start_index - pos] = temp % 10
            c[start_index - pos - 1] += temp // 10
            pos += 1
        while c[0] == 0 and len(c) > 1:
            c.remove(0) 
        c = list(map(lambda x: str(x), c))
        return ''.join(c)

    
    def __mutiply__(self, a, b):
        c = list(map(lambda x: 0, ('0'+ a.strip() + b.strip())))
        a = list(map(lambda x: int(x), a.strip()))
        b = list(map(lambda x: int(x), b.strip()))
        start_index = len(c) - 1
        for i in range(len(a)-1, -1, -1):
            pos = 0
            for j in range(len(b)-1, -1, -1):
                temp = a[i] * b[j] + c[start_index - pos]
                c[start_index - pos] = temp % 10
                c[start_index - pos - 1] += temp // 10
                pos += 1
            start_index -= 1
            while c[0] == 0 and len(c) > 1:
                c.remove(0) 
        c = list(map(lambda x: str(x), c))
        return ''.join(c)
    
if __name__ == '__main__':
    a = '0001'
    b = '0003'
    c = HighAccuracyAlgorithm().__add__(a, b)
    print(c)