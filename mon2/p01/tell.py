a=open('txt.txt','r')
b=a.readline()
print(b)
print(a.tell())
b=a.readline()
print(b)
print(a.tell())
b=a.readline()
print(b)
print(a.tell())
b=a.readline()
print(b)
print(a.tell())
b=a.readline()
print(b)
print(a.tell())
b=a.readline()
print(b)
print(a.tell())
a.close()
a=open('txt.txt','r')
print(a.seek(0,0))
print(a.read(5))
print(a.seek(-4,2))
