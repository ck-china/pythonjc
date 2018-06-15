class SweetPotato:
    def __init__(self):
        self.inf='生地瓜'
        self.lev=0
        self.seas=[]
    def cook(self,tim):
        self.lev += tim
        if self.lev <= 3:
            self.inf='生地瓜'
        elif self.lev <= 5:
            self.inf='半生不熟的地瓜'
        elif self.lev <= 8:
            self.inf='完美的烤地瓜'
        else:
            self.inf='都黑成炭的烂地瓜'
    def seaion(self,sea):
        self.sea=sea
        self.seas.append(self.sea)
        a=""
        for i in self.seas:
            a+=i+','
        a=a[:a.rfind(',')]
        self.inf='加了'+a+self.inf
    def screen(self):
        print(self.inf)
a=SweetPotato()
a.cook(float(input('请输入烤地瓜的时间 : ')))
a.seaion(input('请输入要加入的调料:'))
a.screen()
