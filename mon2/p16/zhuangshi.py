def wai(x):
    def nei(name):
        if name == 'yuangong':
            print('欢迎使用')
            x()
        else:
            print('没有帐号权限，禁止使用！')
    return nei
def wal(x):
    def nei(name):
        if name == 'yuangong':
            print('欢迎使用')
            x()
        else:
            print('没有密码权限，禁止使用！')
    return nei
@wai
@wal
def f1():
    print('-=-=-=-f1已调用-=-=-=-')
f1('yuangong')

