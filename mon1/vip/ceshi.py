import random
a=1
lis=[]
while a <= 5:
    n=random.randint(1,100)
    lis.append(n)
    a+=1
    if lis.count(n) > 1:
        lis.pop
        a-=1
print(lis)

