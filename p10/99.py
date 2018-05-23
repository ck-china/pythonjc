a = 1
b = 1
c = 1
while c <= 9:
    e = 1
    while e < c:
        f=a*e
        print("%d*%d="%(a,e),f,end="\t")
        e=e+1
    d =a*b
    print("%d*%d="%(a,b),d,end="\t")
    a=a+1
    b=b+1
    c=c+1
    print("\n")
