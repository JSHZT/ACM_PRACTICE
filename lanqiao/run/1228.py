while True:
    try:
        n = int(input())
        a_list = list(map(int, input().split()))
        ans = 0
        while len(a_list) > 1:
            a_list.sort()
            x1 = a_list.pop(0)
            x2 = a_list.pop(0)
            ans += x1 + x2
            a_list.append(x1 + x2)
        print(ans)
    except:
        break