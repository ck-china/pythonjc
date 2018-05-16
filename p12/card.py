def card():
    print("*"*50)
    print("         欢迎使用[名片管理系统]V9.9.9.9")
    print('\n')
    print('1.新建名片  \n2.显示全部\n3.查询名片\n4.删除名片\n5.退出系统')
    print('\n')
    print("*"*50)
def add():
    print("添加一份名片")
def quanbu():
    print("显示全部名片")
def search():
    print("查找一份名片")
def del1():
    print("删除名片")
def tuichu():
    print("成功退出名片管理系统")
def add1():#添加信息函数
    gongsi=input("公司的名字:")
    name=input("请输入名字:")
    age=input("请输入年龄:")
    phone=input("请输入联系方式:")
    address=input("请输入地址:")
    zhiwu=input("请输入你的工作:")
def print1():
    print(
card()
while True:
    a=int(input("请选择你需要的操作"))
    if a == 1:
        add()
        add1()
    elif a == 2:
        quanbu()
    elif a == 3:
        serach()
    elif a == 4:
        del1()
    elif a == 5:
        tuichu()
        break
