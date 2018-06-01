a=int(input("要建几层金字塔"))
b=1
while a >= 0:
    print(' '*a,'*'*b)
    a=a-1
    b=b+2
