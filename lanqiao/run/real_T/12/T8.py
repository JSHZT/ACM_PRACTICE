def dfs(u):
    res = 0
    cnt = len(g[u])
    for i in range(len(g[u])):
        res = max(res, dfs(g[u][i])+cnt)
    return res

N = int(input())
g = [[] for _ in range(N+1)]
for i in range(2, N+1):
    temp = int(input())
    g[temp].append(i)
res = dfs(1)
print(res)
