class Potato:
    def __init__(self):
        self.inf='米奇林大厨刚切好的细如丝发的土豆丝'
        self.shijian=0
        self.seaions=[]
    def cook(self,tim):
        self.shijian+=tim
        if self.shijian <= 3:
            self.inf='青涩脆爽的生生生土豆丝'
        elif self.shijian <=10:
            self.inf='稍微软了一点，还是不能吃的土豆丝'
        elif self.shijian <=15:
            self.inf='差一步美满的土豆丝'
        elif self.shijian <=20:
            self.inf='宛如中华小当家他全家附体做的完美的熟土豆丝'
        else:
            self.inf='看不出来是土豆丝的土豆丝？？？？'
    def seaion(self,sea):
        self.seaions.append(sea)
        a=''
        for i in self.seaions:
            a+=i+','
        a=a[:a.rfind(',')]
        self.inf='加了'+a+'的'+self.inf
    def __str__(self):
        return self.inf
a=Potato()
while True:
    a.cook(float(input('请输入炒土豆丝的时间 : ')))
    a.seaion(input('请输入要加入的调料:'))
print(a)

