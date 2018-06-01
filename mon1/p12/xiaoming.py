i=input("公交请选择‘1’，轨道交通请选择‘2’")
if i == "1":
    scard=0.25
    pcard=0.5
    a=input("请问是学生卡还是普通卡（s为学生卡p为普通卡）")
    b=int(input("请输入路程/KM"))
    if a == "s":
        if b <=10:
            x=2
        elif b > 10:
            if (b-10)%5 ==0:
                x=2+(b-10)/5*1
            elif (b-10)%5 !=0:
                x=2+((b-10)//5+1)*1
        x=x*scard
    if a == "p":
        if b <=10:
            x=2
        elif b > 10:
            if (b-10)%5 ==0:
                x=2+(b-10)/5*1
            elif (b-10)%5 !=0:
                x=2+((b-10)//5+1)*1
        x=x*pcard
    print(x)
elif i =="2":
    b=int(input("请输入路程/KM"))
    if b > 0 and b <= 32:
        if b <=6:
            x=3
        elif b > 6 and b <= 12:
            x=4
        elif b > 12 and b <=22:
            x=5
        else:
            x=6
    else:
        if (b-32)%20 ==0:
            x=6+(b-32)//20*1
        else:
            x=6+((b-32)//20+1)*1
    print(x)
