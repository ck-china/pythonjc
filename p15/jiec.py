def diui(a):
    if a >= 1:
        s=a*diui(a-1)
    else:
        s=1
    return(s)
print(diui(5))
