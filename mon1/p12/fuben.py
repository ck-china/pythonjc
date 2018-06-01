def he(x,y):
    z=x+y
    return(z)
def minus(x,y):
    z=x-y
    return(z)
def multiply(x,y):
    z=x*y
    return(z)
def divide(x,y):
    z=x/y
    return(z)
print("欢迎使用国服第一计算器")
a=float(input("请输入第一个数字："))
while True:
    b=input("请输入运算符号:(+ - * /),或者输入‘q’退出")
    if b == "q":
        print("当前运算的结果是：",a)
        break
    c=float(input("请输入第二个数字："))
    if b == "+":
        x=he(a,c)
    elif b == "-":
        x=minus(a,c)
    elif b == "*":
        x=multiply(a,c)
    elif b =="/":
        x=divide(a,c)
    else:
        print("您的输入有误")
    a=x
    print(a)
