class Animal:
    def __init__(self,name):
        self.__name=name
    def ask(self,who):
        if who == '饲养员':
            b=open('txt.txt','r')
            c=b.read()
            if len(c) > 0:
                return c
            else:
                return '还未设置名称'
            b.close
        else:
            return '%s又不认识你'%self.__name
    def change(self,new):
        self.__name=new
        a=open('txt.txt','w')
        a.write(self.__name)
        a.close
        return '名字更改为%s'%self.__name
    '''
    def __del__(self):
        a = open('txt.txt','w')
        a.write(self.name)
        a.close()
        print('关灯咯')
    '''
dog=Animal('哈士奇')
print(dog.change('三傻之首——哈士奇'))
print(dog.ask('草'))
