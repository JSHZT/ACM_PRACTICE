N = 5 * 10**5
far = [0] * (N<<1)

def find(x):
    if(x==far[x]):
        return x
    far[x] = find(far[x])
    return far[x]   

def union(x, y):
    tdx = find(x)
    tdy = find(y)
    if ( tdx != tdy):
        far[tdx] = tdy

while True:
    try:
        for i in range(N<<1):
            far[i] = i
        res = 0
        n, m = map(int, input().split())
        while(m>0):
            m -= 1
            x, y = map(int, input().split())
            if (res): continue
            if(find(x) == find(y) or find(x+N) == find(y+N)):
                res = x
            else:
                union(x, y+N)
                union(x+N, y)
        print(res)
    except:
        break