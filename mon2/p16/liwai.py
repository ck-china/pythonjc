def wai(a,b):
    def nei(x):
        print('y=%d*%d+%d'%(a,x,b))
        y=a*x+b
        return y
    return nei
a=wai(10,5)
print(a(4))

