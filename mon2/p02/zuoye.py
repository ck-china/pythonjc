class ZhiWu:
    def __init__(self,name,gongneng,dongzuo):
        self.name=name
        self.gongneng=gongneng
        self.dongzuo=dongzuo
    def jieshao(self):
        print('我是 %s ,我的作用是 %s'%(self.name,self.gongneng))
    def zhuangtai(self):
        print('%s 正在 %s '%(self.name,self.dongzuo))
    def __str__(self):
        abc=self.name+'正在守护院子,臭傻逼你竟然还在蹦迪土嗨？？？'
        return abc
class JiangShi:
    def __init__(self,name,sudu,fuzhuang):
        self.name=name
        self.sudu=sudu
        self.fuzhuang=fuzhuang
    def jieshao(self):
        print('我是 %s僵尸,我跑得%s'%(self.name,self.sudu))
    def zhuangtai(self):
        print('%s僵尸穿的%s'%(self.name,self.fuzhuang))
a=ZhiWu('向日葵','产阳光','摇头')
a.jieshao()
a.zhuangtai()
b=JiangShi('普通','慢','普普通通')
b.jieshao()
b.zhuangtai()
c=ZhiWu('豌豆射手','发射社会主义豌豆','疯狂摇头吐豆豆')
c.jieshao()
c.zhuangtai()
d=JiangShi('橄榄球','快',' +15华丽的橄榄球运动套装')
d.jieshao()
d.zhuangtai()
print(a)
print(c)
