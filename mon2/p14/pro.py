class Peo(object):
    def __init__(self):
        self.__money=0
    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self,value):
        self.__money=value
a=Peo()
print(a.money)
#a.setmon(999999)
a.money=99999
print(a.money)
