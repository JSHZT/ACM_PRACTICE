class HighAccuracyAlgorithm(object):
    def __add__(self, a, b):
        return
    
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
        c = list(map(lambda x: str(x), c))
        return (''.join(c)).strip('0')
    
if __name__ == '__main__':
    a = '1234'
    b = '5678'
    c = HighAccuracyAlgorithm().__mutiply__(a, b)
    print(c)