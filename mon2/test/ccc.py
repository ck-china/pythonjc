class Shu:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.lis=[]
    def sushu(self):
        for i in range(self.a,self.b+1):
            flag=True
            for y in range(2,11):
                if i % y == 0:
                    flag=False
                    break
            if flag:
                self.lis.append(i)
a=Shu(100,200)
a.sushu()
print(a.lis)
