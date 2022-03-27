dic = {
    '0':2021, '1':2021, '2':2021, '3':2021, 
    '4':2021, '5':2021, '6':2021, '7':2021, 
    '8':2021, '9':2021
}
i = 0
flag = 0
while True:
    i += 1
    temp = list(str(i))
    for j in temp:
        if dic[j] > 0:
            dic[j] -= 1
        else:
            flag = 1
            break
    if flag == 1:
        print(i-1)
        break