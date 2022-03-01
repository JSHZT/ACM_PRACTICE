word_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
             'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def FJ(n):
    if n == 1:
        return word_list[0]
    else:
        return FJ(n-1) + word_list[n-1] + FJ(n-1)
    
while True:
    try:
        n = int(input())
        print(FJ(n))
    except:
        break