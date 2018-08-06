def f1(x):
    def f11():
        print('f1已调用')
    if x == 'yuangong':
        return f11
def f2(x):
    def f22():
        print('f2已调用')
    if x == 'yuangong':
        return f22
def f3(x):
    def f33():
        print('f3已调用')
    if x == 'yuangong':
        return f33
def f4(x):
    def f44():
        print('f4已调用')
    if x == 'yuangong':
       return f44
a=f1('yuangong')
a()
#b=f1('6666')
#b()


