class animal:
    def __init__(self,name):
        self.__name=name
    def pa(self):
        print("%s会爬，爬爬怪"%self.__name)
class dog(animal):
    def jiao(self):
        print('汪汪汪')
gou=dog('花花')
gou.pa()
gou.jiao()
