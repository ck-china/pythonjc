class Nv(object):
    __ls=None
    __tr=True
    def __new__(cls,k):
        if Nv.__ls== None:
            Nv.__ls=object.__new__(cls)
        return Nv.__ls
    def __init__(self,name):
        if Nv.__tr == True:
            self.name=name
            Nv.__tr=False
a=Nv('PM')
b=Nv('hh')
print(a.name)
print(b.name)

