while True:
    s1 = input()
    s2 = input()
    if(s1==s2):
        print(2)
    elif(s1.upper()==s2.upper()):
        print(3)
    elif(len(s1)==len(s2)):
        print(4)
    else:
        print(1)