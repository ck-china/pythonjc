import sys
class people:
    def __init__(self,name):
        self.name=name
class animal:
    def __init__(self,name):
        self.name=name
a=people('wahaha')
b=a
c=b
print(sys.getrefcount(a))
print(sys.getrefcount(b))
print(sys.getrefcount(c))
print(isinstance(a,people))
print(isinstance(b,animal))
