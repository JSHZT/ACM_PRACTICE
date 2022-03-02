t = {
    '01':(1, 0), '10':(0, -1), '0-1':(-1, 0), '-10':(0, 1)
}


def turnleft(x, y):
    x_, y_ = t[str(x)+str(y)]
    return x_, y_

if __name__ == '__main__':
    m, n = map(int, input().split())
    s = []
    for i in range(m):
        s.append(list(map(int, input().split())))
    x = 0
    y = 1
    newx = newy = 0
    while True:
        print(s[newy][newx], end='')
        s[newy][newx] = '0'
        if (not(newx + x < n and newy + y  < m)) or s[newy+y][newx+x]=='0':
            x, y = turnleft(x, y)
            if s[newy+y][newx+x]=='0':
                break
        newx = newx + x
        newy = newy + y
        print(' ', end='')