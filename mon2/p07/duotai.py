class Pig(object):
    def walk(self):
        print('猪走起来屁股一扭一扭')
    def eat(self):
        print('猪吃得多才能长胖卖的多')
class Cow(object):
    def walk(self):
        print('牛走起来慢吞吞的')
    def eat(self):
        print('牛吃草也是慢吞吞的，成熟稳重')
def tools(obj):
    obj.walk()
    obj.eat()
a=Pig()
b=Cow()
tools(a)
tools(b)
