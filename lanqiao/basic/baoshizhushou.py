dic = {
    '0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five',
    '6':'six',  '7':'seven',  '8':'eight',  '9':'nine',  '10':'ten',  
    '11':'eleven', '12':'twelve', '13':'thirteen', '14':'fourteen', '15':'fifteen',  
    '16':'sixteen',  '17':'seventeen',  '18':'eighteen',  '19':'nineteen',  '20':'twenty',
    '30':'thirty', '40':'forty', '50':'fifty'
}
while True:
    try:
        h, m = map(int, input().split())
        h_ = m_ =0
        ans = ''
        if h > 20 and h < 24:
            h_ = h - (h // 10 * 10)
            h = h - h_
        if m>20 and m<60:
            m_ = m - (m // 10 * 10)
            m = m - m_
        if m == 0:
            if h_ == 0:
                ans += dic[str(h)] + ' ' + "o'clock"
            else:
                ans += dic[str(h)] + ' ' + dic[str(h_)]
        else:
            if m_ == 0:
                if h_ == 0:
                    ans += dic[str(h)] + ' ' + dic[str(m)]
                else:
                    ans += dic[str(h)] + ' ' + dic[str(h_)] + ' ' + dic[str(m)]
            else:
                if h_ == 0:
                    ans += dic[str(h)] + ' ' + dic[str(m)] + ' ' + dic[str(m_)]
                else:
                    ans += dic[str(h)] + ' ' + dic[str(h_)] + ' ' + dic[str(m)] + ' ' + dic[str(m_)]
        print(ans)
    except:
        break