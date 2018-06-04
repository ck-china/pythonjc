class car:
    def __init__(self,pinpai,jiage,chexing,lunzi):
        self.pinpai=pinpai
        self.jiage=jiage
        self.chexing=chexing
        self.lunzi=lunzi
    def Q(self):
        print('%s的轮子肯定有%d个啊,毕竟花%d元买的'%(self.chexing,self.lunzi,self.jiage))
a=car('大运',300000,'大运重卡',12)
a.Q()
b=car('蹦蹦',15000,'时风',3)
b.Q()
