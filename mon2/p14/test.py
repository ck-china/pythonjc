class Person(object):
    def __init__(self,name,age,sex):
        self.name=name
        self._age=age
        self.__sex=sex
    def show(self):
        print(self.name)
        print(self._age)
        print(self.__sex)
    def _work(self):
        print('true work')
    def __work(self):
        print('false work')
    def whatwork(self):
        self._work()
        self.__work()
a=Person('张翠花',11,'女')
a.show()
a.whatwork()
