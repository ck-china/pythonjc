import random
b=random.randint(1,100)
for c in range(1,11):
    a=int(input("请输入一个数:"))
    if a<=100:
        if a >b:
            if a-b<=5:
                print("大了一点!")
            elif a-b<=20:
                print("有点大!")
            else:
                print("太大了！")
        elif a<b:
            if b-a<=5:
                print("小了一点!")
            elif b-a<=20:
                print("有点小!")
            else:
                print("太小了!")
        else:
            print("恭喜你猜中了！")
            break
    else:
        print("不再范围")
    if c==10:
        print("次数用完，游戏结束")
