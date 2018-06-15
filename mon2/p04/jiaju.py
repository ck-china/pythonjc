class House:
    def __init__(self,large,addr):
        self.large=large
        self.addr=addr
        self.item=[]
    def tianjia(self,bed):
        if self.large > bed.area:
            self.large-=bed.area
            self.item.append(bed.name)
        else:
            print('穷比，房子太小了！')
    def __str__(self):
        return '我的房子有%d平米,位于%s,里面有%s'%(self.large,self.addr,str(self.item))
class Bed:
    def __init__(self,area,name):
        self.area=area
        self.name=name
    def __str__(self):
        return '床是%s,大小是%dcm'%(self.name,self.area)
a=House(150,'承德避暑山庄')
b=Bed(220,'寒冰床')
a.tianjia(b)
c=Bed(210,'席梦思大床')
a.tianjia(c)
print(a)
