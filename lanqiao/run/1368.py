while True:
    try:
        N, M = map(int, input().split())
        a_list = [0] * (N+1)
        b_list = [0] * (N+1)
        c_list = [0] * (N+1)
        while(M > 0):
            M -= 1
            l, r, s, e = map(int, input().split())
            d = (e - s) / (r - l)
            c_list[l] += s
            c_list[l+1] += d - s
            try:
                c_list[r+1] -= e + d
                c_list[r+2] += e
            except:
                pass
        sums = 0
        for i in range(1, N+1):
            b_list[i] = b_list[i-1] + c_list[i]
            a_list[i] = b_list[i] + a_list[i-1]
            sums += a_list[i]
        print(int(sums), end='')
    except:
        break
