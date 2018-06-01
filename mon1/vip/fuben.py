dic={'d':0}
def cc():
    money=0
    c1=int(input('time1'))
    c2=int(input('time2'))
    if c1 >=0 and c1 <=24 and c2 >=0 and c2 <=24:
        if c1 >=7 and c1 <=20 and c2 >7 and c2 <=20:
            money=(c2-c1)*5
            print(money)
            dic['d']=dic['d']+money
        elif c1 >0 and c1 < 7 or c1 >= 20 and c1 <=24 and c2 > 0 and c2 <= 7 or c2 >= 20 and c2 <=24:
            if c1 > 0 and c1 < 7 and c2 >0 and c2 <=7:
                money=(c2-c1)*5
            elif c1 >=20 and c1 <=24 and c2 > 0 and c2 <=7:
                money=(24-c1+c2)*5
            elif c1 >= 20 and c2 >= 20:
                money=(c2-c1)*5
            else:
                print('error')
            print(money)
            dic['d']=dic['d']+money
        else:
            print("error")
    else:
        print('error')
while True:

    cc()
    print(dic['d'])
