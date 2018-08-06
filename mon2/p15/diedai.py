from collections import Iterator
ls=[]
a,b=0,1
while b<100:
    ls.append(b)
    a,b=b,a+b
ls=iter(ls)
for i in ls:
    print(i)
