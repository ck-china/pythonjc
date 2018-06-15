class stu:
    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age
        self.chengji={}
    def chengjijia(self,kemu,defen):
        self.chengji[kemu]=defen
    def __str__(self):
        return '姓名: '+self.name+'\n性别: '+self.sex+'\n年龄: '+self.age+'\n成绩 : '+self.chegnji.items
a=stu('ming','nan','21')
b=stu('gang','nan','18')
c=stu('hua','nv','20')
for o in range(1,6):
    x=input('keMu:')
    y=input('deFen:')
    a.chengjijia(x,y)
ss=open('www.txt','w')
ss.write(a)
ss.close
