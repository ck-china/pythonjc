class peo:
    def __init__(self,name):
        self.name=name
        self.blood=100
        self.guns=[]
    def chiqiang(self,qiang):
        self.qiang=qiang
        self.guns.append(self.qiang)
    def __str__(self):
        return '正前方有%s，悠闲的挑逗这你家的哈士奇，老王有%d血量'%(self.name,self,blood)
    def zhuangdan(self,):
        pass
    def zhuangdanjia(self,):
        pass
    def kaiqiang(self,):
        pass
class zidan:
    def __init__(self,shanghai):
        self.shanghai=shanghai
    def tanchu(self,):
        pass
class danjia:
    def __init__(self,cap):
        cap=25
        self.cap=cap
    def shangdan(self,n):
        self.yv=0
        if n <= cap:
            self.yv += cap
        else:
            print('弹夹容量只有25哦')
    def shechu(self,m):
        if m <= self.yv:
            print('咻咻咻,疯狂的射出了%d发子弹'%m)
            self.yv -= m
        else:
            print('没那么多子弹啊')
class gun:
    def __init__(self,jia):
        self.jia=jia
    def shangtang(self,):
        pass
    def sheji(self,):
        pass

