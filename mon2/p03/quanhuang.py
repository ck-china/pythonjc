class juese:
    def __init__(self,name):
        self.name=name
    def ran(self):
        print('%s快速跑动'%self.name)
    def yaobai(self):
        print('%s左右摇摆'%self.name)
    def tui(self):
        print('%s使出无影腿'%self.name)
    def quan(self):
        print('%s使出通臂拳'%self.name)
def lianzhao1(aa):
    aa.ran()
    aa.yaobai()
    print('%s用出了失传已久的 真 × 反复横跳'%aa)
def lianzhao2(aa):
    aa.ran()
    aa.tui()
    print('%s用出了失传已久的 真 × 飞起一JIO'%aa)
def lianzhao3(aa):
    aa.ran()
    aa.quan()
    print('%s用出了失传已久的 真 × 马氏跑跳杀'%aa)
jing=juese('草薙京')
shen=juese('八神庵')
lianzhao1(jing)
lianzhao2(shen)
lianzhao3(jing)
