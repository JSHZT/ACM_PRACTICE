inf = 2**30
n = 21

def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

def make_a_graph(G):
    for i in range(n):
        for j in range(i+1, n):
            if(gcd(i+1, j+1) == 1):
                G[i][j] = 1
                G[j][i] = 1
    return G
if __name__ == '__main__':
    ans = 0
    
    G = [[0] * n for _ in range(n)]
    dp = [[0] * (n)for i in range(2 ** n)]
    G = make_a_graph(G)
    dp[1][0] = 1
    for state in range(1, 1<<n):
        for now in range(21):
            if((state>>now) & 1 and dp[state][now]):
                for next in range(21):
                    if(((state>>next) & 1 ==0 ) and (G[now][next] == 1)):
                        dp[state | 1<<next][next] += dp[state][now]
    
    for i in range(21):
        ans += dp[(1<<n)-1][i]
        
print(ans)
#计算结果 881012367360