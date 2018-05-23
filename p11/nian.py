a=int(input("请输入2000到3000之间的年份来判断平年闰年："))
if a >=2000 and a <= 3000:
    while a <=3000:
        if a%4 == 0 and a%100 != 0:
            print("%d年是闰年"%a)
        elif a%400 == 0:
            print('%d年是闰年'%a)
        else:
            print('%d年是平年'%a)
        a=a+1
else:
    print("输入的年份有误")
