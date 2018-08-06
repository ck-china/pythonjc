def wai(x):
    def nei(name):
        if name == 'yuangong':
            print('欢迎使用')
            x()
        else:
            print('没有权限，禁止使用！')
    return nei

@wai
def f1():
    print('====*f1*====')
@wai
def f2():
    print('====*f2*====')
#a=wai()
#a(input('请输入姓名验证 :'))
f1('yuangong')
