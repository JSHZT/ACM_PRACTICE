while True:
    try:
        times = int(input())//1000
        h = times // 3600
        if h > 23:
            h = h % 24
        m = times % 3600 // 60
        s = times % 3600 % 60
        z = '0'
        if h < 10:
            h = z+str(h)
        if m < 10:
            m = z+str(m)
        if s < 10:
            s = z+str(s)
        print("{}:{}:{}".format(h, m, s)) 
    except:
        break