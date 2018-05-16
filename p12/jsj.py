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
a=int(input("请输入第一个数字："))
b=input("请输入符号:(+ - * /)")
c=int(input("请输入第二个数字："))
if b == "+":
    x=he(a,c)
    print(a)
elif b == "-":
    x=minus(a,c)
    print(x)
elif b == "*":
    x=multiply(a,c)
    print(x)
elif b =="/":
    x=divide(a,c)
    print(x)
else:
    print("输入的符号有误")
