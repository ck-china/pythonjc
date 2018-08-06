def wai(start=0):
    def nei():
        nonlocal start
        start+=1
        print(start)
        return start
    return nei
a=wai(1)
print(a())
print(a())
b=wai(5)
print(b())
