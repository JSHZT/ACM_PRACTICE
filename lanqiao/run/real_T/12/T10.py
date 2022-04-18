def comput_nums(n):
    if n == 1:
        return list({'()'})
    res = set()
    for i in comput_nums(n-1):
        for j in range(len(i)+2):
            res.add(i[:j] + '()' + i[j:])
    return list(res)

while True:
    try:
        a_list = list(input())
        l = a_list.count('(')
        r = a_list.count(')')
        n = max(l, r)

        if n == 1:
            print('1')
            break
        ans = len(comput_nums(n))
        print(ans)
    except:
        break