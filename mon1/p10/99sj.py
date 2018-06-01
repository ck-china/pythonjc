x=1
while  x <= 9:
    y=1
    while y <= x:
        print("%d*%d=%d"%(y,x,x*y),end="\t")
        y=y+1
    x=x+1
    print("\n")
