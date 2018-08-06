class Ck(object):
    def __init__(self):
        self.name = "ck"
        print('%s已经创建'%self.name)
    def __str__(self):
        print('这是str方法')
        return self.name
    def __new__(cls):
        print('这是new方法')
        return object.__new__(cls)
    def __del__(self):
        print('这是del方法')
class Son(Ck):
    pass
a=Son()
print(a)
