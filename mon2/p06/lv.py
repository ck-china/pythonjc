class Ma:
    def run(self):
        print('跑得快')
    def jiao(self):
        print('反正和驴叫得不一样')
class lv:
    def naili(self):
        print('持久力强')
    def jiao(self):
        print('阿欧阿欧啊欧啊欧')
class Luozi(Ma,lv):
    def jiao(self):
        super(Luozi,self).jiao()
a=Luozi()
a.run()
a.naili()
a.jiao()
