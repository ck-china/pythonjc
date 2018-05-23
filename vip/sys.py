#网吧收银系统,
def guize():
         print("网吧的收费规则：普通用户，白天时段7点到20点，五元一小时，晚上段20点到第二天7点，晚段支持包夜，20点开始包夜20元，21点开始包夜18元，22点以后包夜16元 会员一律九折")
import fzzl
fzzl.fzzl()
dic={"xx":0}
def hello():
    print("*"*30)
    print("*"*30)
    print("欢迎光临真皮网咖")
def yunSuanp():
    c1=float(input("请问您开始上网的时间是：（例子1 八点三十为8.30格式）"))
    if c1 % 1 == 0:
        c1 = c1
    elif c1 % 1 < 0.6:
        c1=c1//1+c1%1/0.6
    else:
        print("error")
    c2=float(input("请问您预计离开的时间是：（例子2 下午四点二十为16.20）"))
    if c2 % 1== 0:
        c2 = c2
    elif c2 % 1 < 0.6:
        c2=c2//1+c2%1/0.6
    else:
        print("error")
    if c1 >= 0 and c1 <=24 and c2 >=0 and c2 <=24:
        if c1 >= 20 and c1 <= 24 or c1 > 0 and c1 < 7 and c2 > 0 and c2 <= 7 or c2 <= 24 and c2 >= 20:
            if c1 >=20 or c1 < 7:
                d=input("请问要办理包夜吗？要为 y  不用 为 no ：")
                if d == "y":
                    if c1 >=20 and c1 < 21:
                        money=20
                    elif c1 >= 21 and c1 < 22:
                        money=18
                    else:
                        money=16
                elif c1 < 24 and c1 >=20 and c2 < 24 and c2 > 20 :
                    money=(c2-c1)*5
                elif c1 <= 24 and c1 >=20 and c2 >0 and c2 <= 7:
                    money=(24-c1+c2)*5
                elif c1 >= 0 and c1 <= 7 and c2 >=0 and c2 <= 7:
                    money=(c2-c1)*5
        elif c1 >= 7 and c2 <= 20:
            money=(c2-c1)*5
    else:
        print("输入的时间有误")
    dic['xx']=dic['xx']+money
    return(money)
def yunSuanvip():
    c1=float(input("请问您开始上网的时间是：（例子1 八点三十为8.30格式）"))
    if c1 % 1 == 0:
        c1 = c1
    elif c1 % 1 < 0.6:
        c1=c1//1+c1%1/0.6
    else:
        print("error")
    c2=float(input("请问您预计离开的时间是：（例子2 下午四点二十为16.20）"))
    if c2 % 1== 0:
        c2 = c2
    elif c2 % 1 < 0.6:
        c2=c2//1+c2%1/0.6
    else:
        print("error")
    if c1 >= 0 and c1 <=24 and c2 >=0 and c2 <=24:
        if c1 >= 20 and c1 <= 24 or c1 > 0 and c1 < 7 and c2 > 0 and c2 <= 7 or c2 <= 24 and c2 >= 20:
            if c1 >=20 or c1 < 7:
                d=input("请问要办理包夜吗？要为 y  不用 为 no ：")
                if d == "y":
                    if c1 >=20 and c1 < 21:
                        money=20
                    elif c1 >= 21 and c1 < 22:
                        money=18
                    else:
                        money=16
                elif c1 < 24 and c1 >=20 and c2 < 24 and c2 > 20 :
                    money=(c2-c1)*5
                elif c1 <= 24 and c1 >=20 and c2 >0 and c2 <= 7:
                    money=(24-c1+c2)*5
                elif c1 >= 0 and c1 <= 7 and c2 >=0 and c2 <= 7:
                    money=(c2-c1)*5
        elif c1 >= 7 and c2 <= 20:
            money=(c2-c1)*5
    else:
        print("输入的时间有误")
    money=money*0.9
    dic['xx']=dic['xx']+money
    return(money)
def lingshi():
    ss=input("请问需要购买什么种类：1.零食 2.饮料")
    if ss == "1":
        s=input("零食有泡面，火腿，瓜子，薯片，请问需要什么?")
        if s == "泡面":
            print("泡面五元一桶")
            money=5
        elif s == "火腿":
            print("火腿一元一个")
            money=1
        elif s == "瓜子":
            print("瓜子两元一包")
            money=2
        elif s == "薯片":
            print('薯片三元一包')
            monry=3
        else:
            print("输入有误，自动弹回首页")
    elif ss == "2":
        s=input("饮料有矿泉水，可乐，雪碧，柠檬茶，请问需要什么?")
        if s == "矿泉水":
            print('矿泉水一元一瓶')
            money=1
        elif s == '可乐':
            print('可乐两元五一瓶')
            money=2.5
        elif s == '雪碧':
            print('雪碧三元一瓶')
            money=3
        elif s == '柠檬茶':
            print('柠檬茶五元一杯')
            money = 5
        else:
            print('输入有误，自动弹回首页')

    else:
        print("您的输入有误，自动弹回首页")
    global money
    dic['xx']=dic['xx']+money
hello()
while True:
    a=input("上网请输入     1 \n购买商品请输入 2 \n退出请输入     q :")
    if a == "1":
        guize()
        b=input("普通用户请输入 p ，会员请输入 vip：")
        if b == "p":
            yunSuanp()
            print('当前消费%.2f元'%dic['xx'])
        elif b == "vip":
            yunSuanvip()
            print('当前消费%.2f元'%dic['xx'])
        else:
            print("输入有误")
        print("当前需要支付%f元"%dic['xx'])
    elif a == "2":
        lingshi()
        print('当前消费%.2f元'%dic['xx'])
    elif a == "q":
        print("退出成功")
        print('共消费%.2f元'%dic['xx'])
        print('欢迎下次光临')
        break
    else:
        print("输入有误，请重新输入")
    print("*"*30)
    print("*"*30)
