while True:
    try:
        N, Q = map(int, input().split())
        a_list = list(map(int, input().split()))
        b_list = [0]*N
        while(Q>0):
            Q -= 1
            l, r, x = map(int, input().split())
            b_list[l-1] += x
            if r<N:
                b_list[r] -= x
        for i in range(1, N):
            b_list[i] += b_list[i-1]
        for i in range(N):
            print(max(b_list[i]+a_list[i], 0), end=" ")
    except:
        break