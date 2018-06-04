a=open('txt.txt','r')
b=open('副本'+a.name,'w')
c=a.read()
b.write(c)
a.close
b.close
