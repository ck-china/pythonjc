class Work:
    def __init__(self,name,money):
        self.name=name
        self.money=money
    def setmon(self,newmoney):
        if newmoney > self.money:
            self.money=newmoney
        else:
            print('拒绝')

a=Work('马化腾',100)
print(a.money)
a.setmon(float(input('你要把我的工资调到多少？？？')))
print(a.money)
