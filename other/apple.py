while True:
    try:
        n, m = map(int, input().split())
        a_list = [0] * (n+1)
        b_list = [0] * (n+2)
        for i in range(m):
            l, r, c = map(int, input().split())
            b_list[l] += c
            b_list[r+1] -= c
        for i in range(1, n+1):
            a_list[i] = a_list[i-1] + b_list[i]
            print(a_list[i], end=' ')
    except:
        break