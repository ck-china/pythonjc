class DogCk(object):
    __flg = None
    def __init__(self,name):
        self.name =name
    def __new__(cls,name):
        if DogCk.__flg == None:
            DogCk.__flg = object.__new__(cls)
        return DogCk.__flg
a=DogCk('ck')
b=DogCk('ck')
print(id(a))
print(id(b))
