class banji:
    def __init__(self,banzhuren,bianhao):
        self.banzhuren=banzhuren
        self.bianhao=bianhao
        self.lis=[]
class stu:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        self.chengjis={}
class chengji:
    def __init__(self,yvwen,cj1,shuxue,cj2,yingyv,cj3):
        self.kemu1=yvwen
        self.__cj1=cj1
    def getcj(self,kemu,chengji):
        if kemu == self.kemu:
            print('%s的成绩是%S'%(self.kemu,self.__chengji))
        else:
            print('科目不对')


