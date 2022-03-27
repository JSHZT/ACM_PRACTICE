def compute_minb(a, b):
    temp = max(a, b)
    newt = temp
    i = 1
    while True:
        newt = temp * i
        if newt % b== 0 and newt % a == 0:
            break
        else:
            i += 1
    return newt

def Floyd_wallshall(G):
    for i in range(2021):
        for j in range(2021):
            for k in range(2021):
                G[i][j] = min(G[i][j], G[i][k] + G[k][j])
    return G
if __name__ == '__main__':
    G = [[2**30]*2021 for _ in range(2021)]

    for i in range(2021):
        for j in range(i, i + 22):
            try:
                G[i][j] = compute_minb(i+1, j+1)
                G[j][i] = G[i][j]
            except:
                pass
    G = Floyd_wallshall(G)
    print(G[0][2020])
#算出来  10266837