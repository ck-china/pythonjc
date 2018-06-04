class jiese:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height
    def jieshao(self):
        print('我是 %s ，今年 %d岁,体重 %d公斤'%(self.name,self.age,self.height))
a=jiese('东丈',21,65)
a.jieshao()
