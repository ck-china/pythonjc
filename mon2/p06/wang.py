class Wang:
    def __init__(self):
        self.xing='wang'
    def texing(self):
        print('住你隔壁我姓%s'%self.xing)
class son(Wang):
    pass
a=son()
print(a.xing)
a.texing()
