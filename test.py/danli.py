def One(obeject):
    __flg=None
    def __init__(self):
        pass
    def __new__(cls,*k):
        if cls.__flg == None:
            cls.__flg = object.__new__(cls,*K)
        return cls.__flg
a=One(1)
b=One(2)
print(a)
print(b)
