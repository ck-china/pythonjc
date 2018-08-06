class PeopleCk(object):
    def __init__(self):
        self.__sex = '男'
    def set(self,xingbie):
        self.__sex == xingbie
    def get(self):
        return self.__sex
class ZhangSan(PeopleCk):
    __money =100
    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self,money):
        self.__money=money
a=ZhangSan()
print(a.money)
a.money=9999
print(a.money)


