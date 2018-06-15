class Test(object):
    __ins=None
    __ins_name=True
    def __init__(self,name):
        if Test.__ins_name == True:
            self.name=name
            Test.__ins_name=False
        print('__init__ is called')
    def __new__(cls,k):
        if cls.__ins == None:
            cls.__ins=object.__new__(cls)
            print('__new__is called')
        return cls.__ins
a=Test('xhh')
b=Test('ll')
print(a.name,b.name)
print(id(a))
print(id(b))
