while True:
    try:
        T = int(input())
        ans = []
        for _ in range (T):
            num_list = list(map(int, input().split()))
            lens = len(num_list)
            sum_ = 0
            for j in range(1, lens):
                sum_ = sum_ ^ num_list[j]
            if sum_ == 0:
                ans.append('0')
                break
            for i in range(19, -1, -1):
                cnt_1 = 0
                cnt_0 = 0
                for k in range(1, lens):
                    if (num_list[k] >> i & 1 == 1):
                        cnt_1 += 1
                    else:
                        cnt_0 += 1
                if cnt_1 % 2 == 0:
                    continue
                elif cnt_1 == 1:
                    ans.append('1')
                    break
                elif(cnt_1 % 2 == 1 and cnt_0 % 2 == 0):
                    ans.append('1')
                    break
                elif(cnt_1 % 2 == 1 and cnt_0 % 2 == 1):
                    ans.append('-1')
                    break
        for i in ans:
            print(i, end='\n')
    except:
        break