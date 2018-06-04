class Dog:
    def eat(self):
        print('%s是狗，改不了吃屎'%self.name)
    def drink(self):
        print('%s啥都爱喝'%self.name)
    def jieshao(self):
        print('我是 %s ，今年 %d 岁了'%(self.name,self.age))
a=Dog()
a.name='哈士奇'
a.age=3
a.eat()
a.drink()
a.jieshao()
