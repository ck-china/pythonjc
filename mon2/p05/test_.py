class Peo():
    def __init__(self,name,sal):
        self.__name=name
        self.__sal=sal
    def get_peo(self):
        return self.__name
    def set_sal(self,new):
        self.__sal=new
        return self.__sal
a=Peo('烂精灵',500)
print(a.get_peo())
print(a.set_sal(1000))
