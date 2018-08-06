def aaa(self):
    print('aaa')
Test=type('Test',(object,),{'a':aaa})
xhh=Test()
print(Test)
print(xhh)
print(xhh.a())

