try:
    class Pro(object):
        __a=None
        __b=True
        def __new__(cls,k):
            if Pro.__a == None:
                Pro.__a=object.__new__(cls)
            return Pro.__a
        def __init__(self,name):
            if Pro.__b == True:
                self.name=name
                print('__init__ is called')
                Pro.__b=False
        def yunsuan(self):
            self.one=float(input('请输入第一个运算数:'))
            self.fuhao=input('请输入运算符号 + - × / :')
            self.two=float(input('请输入第二个运算数:'))
            if self.fuhao == '+':
                print('%d + %d = %d'%(self.one,self.two,self.one+self.two))
            elif self.fuhao == '-':
                print('%d - %d = %d'%(self.one,self.two,self.one-self.two))
            elif self.fuhao == '*':
                print('%d * %d = %d'%(self.one,self.two,self.one*self.two))
            elif self.fuhao == '/':
                print('%d / %d = %d'%(self.one,self.two,self.one/self.two))
            else:
                print('符号输入有误')
    jsj=Pro('小霸王')
    print(jsj.name)
    jsj.yunsuan()
except Exception as yc:
    print('有异常 : %s'%yc)
