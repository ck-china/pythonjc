class Car(object):
    def __init__(self,name):
        self.name=name
    def run(self):
        return '普通汽车普通的飞奔'
class DaZhong(Car):
    def run(self):
        return '大众汽车大众化，也是普通的飞奔'
class Bmw(Car):
    def run(self):
        return '宝马汽车，帅气的飞奔'
class BenChi(Car):
    def run(self):
        return '奔驰汽车，酷酷的飞奔'
class Peo(object):
    def __init__(self,name):
        self.name=name
    def kaiche(self,che):
        print('%s载着美女，开着%s'%(self.name,che.run()))
a=Peo('程海龙')
car=Car('普通汽车')
dz=DaZhong('大众汽车')
bm=Bmw('宝马X7')
bc=BenChi('奔驰s9')
a.kaiche(car)
