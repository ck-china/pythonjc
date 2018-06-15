class MyError(Exception):
    def __init__(self,error):
        self.name=error
def get_pwd():
    pwd = input('请输入密码： ')
    if len(pwd) < 6:
        raise MyError('密码不能少于六位数!')
try:
    get_pwd()
except Exception as a:
    print('抓住了异常！%s'% a)
