while True:
    n = int(input())
    ang = []
    for i in range(n):
        ang.append(list(map(int, input().split())))
    dp = [[0] * (n+1) for i in range(n+1)]
    dp[1][1] = ang[0][0]
    l = 0
    r = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            try:
                dp[i][j] = ang[i-1][j-1] + max(dp[i-1][j], dp[i-1][j-1])
            except:
                break
    if n % 2 == 1:
        print(dp[n][n // 2 + 2])
    else:
        print(max(dp[n][n // 2 + 1], dp[n][n // 2 + 2]))
        