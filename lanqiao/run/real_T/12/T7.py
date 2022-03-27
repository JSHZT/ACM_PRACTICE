from math import sqrt
while True:
    try:
        N = int(input())
        n = [1]
        c = 1
        while c < 1900:
            n = [1] + [n[j] + n[j+1] for j in range(len(n)-1)] + [1]
            if N in n[:]:
                break
            else:
                c += 1
        if c == 1900:
            k = int(sqrt(N*2))
            while (k*(k-1)//2) < N: ##计算第三项，C(n, 2), 第四项一定比最大范围大不考虑
                k += 1
            if (k*(k-1)//2) == N:
                print(k*(k+1)//2+3)
            else:
                print(N*(N+1)//2+2)
        for i in range(len(n)):
            if n[i] == N:
                print(c*(c+1)//2+i+1)
    except:
        break