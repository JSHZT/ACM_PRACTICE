ans = [[0] * 10000 for i in range(10000)]
ans[0][0] = 1
state = -1
i = 0
j = 1
nums = 2
while True:
    state = -state
    if state == 1:
        while i >= 0 and j >= 0:
            ans[i][j] = nums
            nums += 1
            i += 1
            j -= 1
        j = 0
    elif state == -1:
        while i >= 0 and j >= 0:
            ans[i][j] = nums
            nums += 1
            i -= 1
            j += 1
        i = 0
            