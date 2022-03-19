class Solution(object):
    def lemonadeChange(self, bills):
        dic_bill = {
            '5':0,
            '10':0,
            '20':0
        } 
        if bills[0] != 5:
            return False
        for i in bills:
            dic_bill[str(i)] += 1
            if i == 10:
                if dic_bill['5'] >=1:
                    dic_bill['5'] -= 1
                else:
                    return False
            elif i == 20:
                if dic_bill['10'] >= 1 and dic_bill['5'] >= 1:
                    dic_bill['5'] -= 1
                    dic_bill['10'] -= 1
                elif dic_bill['5'] >= 3:
                    dic_bill['5'] -= 3
                else:
                    return False
        return True
    
   