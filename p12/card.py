import fzzl
fzzl.fzzl()
def card():
    print("*"*50)
    print("         欢迎使用[名片管理系统]V9.9.9.9")
    print('\n')
    print('1.新建名片  \n2.显示全部\n3.查询名片\n4.删除名片\n5.修改名片\n6.退出系统')
    print('\n')
    print("*"*50)
def add():
    print("添加一份名片")
def quanbu():
    print("显示全部名片")
def search():
    print("查找一份名片")
def gai():
    print("修改名片")
def del1():
    print("删除名片")
def tuichu():
    print("成功退出名片管理系统")
def xinxi():
    dic1={}
    b=input("请输入姓名:")
    age=input("请输入年龄:")
    d=input("请输入公司:")
    e=input("请输入地址:")
    f=input("请输入联系方式:")
    g=input("请输入电子邮箱:")
    h=input("请输入你的职位:")
    print("*"*50)
    dic1 = {"姓名":b,"年龄":age,"职位":h,"电子邮箱":g,"公司":d,"地址":e,"联系方式":f}
    lis.append(dic1)
    print(dic1)
    print("名片创建成功")
def search2():
    s=input("请输入查询的姓名:")
    for dic1 in lis:
        if s == dic1['姓名']:
            print(dic1)
            print("*"*50)
            print("*"*50)
            print("                     ","公司：%s"%dic1["公司"])
            print("")
            print(" 姓名：%s"%dic1["姓名"],"  "                  "职位：%s"%dic1["职位"])
            print(" 年龄：%s"%dic1["年龄"])
            print(" 住址：%s"%dic1["地址"])
            print(" 联系方式：%s"%dic1["联系方式"])
            print(" E-mail：%s"%dic1["电子邮箱"])
            print("*"*50)
            print("*"*50)
        elif s != dic1['姓名']:
            print("该用户不存在")
def gai():
    s=input("请输入被修改人的姓名:")
    ss=input("请输入要修改项目的原内容")
    for dic1 in lis:
        if s == dic1['姓名']:
            if ss == dic1["公司"]:
                sss=input("请输入新的内容")
                dic1["公司"]=sss
                print("修改成功")
            elif ss == dic1["姓名"]:
                sss=input("请输入新的内容")
                dic1['姓名']=sss
                print("修改成功")
            elif ss == dic1["年龄"]:
                sss=input("请输入新的内容")
                dic1['年龄']=sss
                print("修改成功")
            elif ss == dic1['职位']:
                sss=input("请输入新的内容")
                dic1['职位']=sss
                print("修改成功")
            elif ss == dic1['电子邮箱']:
                sss=input("请输入新的内容")
                dic1['电子邮箱']==sss
                print("修改成功")
            elif ss == dic1['地址']:
                sss=input("请输入新的内容")
                dic1['地址']=sss
                print("修改成功")
            elif ss == dic1['联系方式']:
                sss=input("请输入新的内容")
                dic1['联系方式']=sss
                print("修改成功")
            else:
                print("输入的信息有误")
        elif s != dic1['姓名']:
            print("该用户不存在")
def shanC():
    s=input("请输入要删除的用户名:")
    for dic1 in lis:
        if s == dic1['姓名']:
            lis.remove(dic1)
            print("删除成功")
        else:
            print("该用户不存在")
def showall():
    for dic1 in lis:
        print(dic1)
        print("*"*50)
        print("*"*50)
        print("                     ","公司：%s"%dic1["公司"])
        print("")
        print(" 姓名：%s"%dic1["姓名"],"  "                  "职位：%s"%dic1["职位"])
        print(" 年龄：%s"%dic1["年龄"])
        print(" 住址：%s"%dic1["地址"])
        print(" 联系方式：%s"%dic1["联系方式"])
        print(" E-mail：%s"%dic1["电子邮箱"])
        print("*"*50)
        print("*"*50)
card()
lis=[]
while True:
    a=int(input("请选择你需要的操作"))
    if a == 1:
        add()
        xinxi()
    elif a == 2:
        quanbu()
        print(lis)
        showall()
    elif a == 3:
        search()
        search2()
    elif a == 4:
        del1()
        shanC()
    elif a == 5:
        gai()
    elif a == 6:
        tuichu()
        break
