def swap(li, a, b):
    temp = li[a]
    li[a] = li[b]
    li[b] = temp
    

while True:
    try:
        lens = int(input())
        s_in = list(input())
        k = 0
        count = [0 for i in range(26)]
        for i in s_in:
            count[ord(i)-97] += 1
        for i in count:
            if(i % 2 == 1):
                k += 1
        if(k>1):
            print("Impossible") 
        else:
            k=0
            l = 0 
            r = lens-1
            mid = l + ((r - l) >> 1)
            while l < mid:
                if s_in[l] == s_in[r]:
                    l += 1
                    r -= 1
                else:
                    temp = r - 1
                    while temp > l:
                        if s_in[temp] == s_in[l]:
                            break
                        temp -= 1
                    if temp == l:
                        while temp < mid:
                            swap(s_in, temp, temp+1)
                            k += 1
                            temp += 1
                    else:
                        while temp < r:
                            swap(s_in, temp, temp+1)
                            k += 1
                            temp += 1
            print(k)   
            print(''.join(s_in))     
    except:
        break