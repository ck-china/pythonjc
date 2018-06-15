class name_Error(Exception):
    def __init__(self,error):
        self.error=error
class Pwd_error(Exception):
    def __init__(self,error):
        self.error=error
def Login():
    name=input('请输入用户名:')
    if len(name) < 1:
        raise name_Error('用户名不能为空!')
    else:
        a=open('name.txt','w')
        a.write(name)
        pwd=input('请输入密码:')
        if len(pwd) <6:
            raise Pwd_Error('密码长度不能少于六位！')
        else:
            b=open('pwd.txt','w')
            b.write(pwd)
        a.close()
        b.close()
def Denglu():
    name=input('请输入用户名:')
    if len(name) < 1:
        raise name_Error('用户名不能为空!')
    else:
        a=open('name.txt','r')
        c=a.read()
        if name == c:
            pwd=input('请输入密码:')
            if len(pwd) <6:
                raise name_Error('密码长度不能少于六位！')
            else:
                b=open('pwd.txt','r')
                d=b.read()
                if pwd == d:
                    print('登录成功，欢迎%s !!!'%name)
                else:
                    raise Pwd_Error('密码验证错误!')
        else:
            raise name_Error('用户名验证错误!')
        a.close()
        b.close()
Login()
Denglu()


