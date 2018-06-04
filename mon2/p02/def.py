def myself(old):
    a=open(old,'r')
    x=old.rfind('.')
    head=old[:x]
    kuozhan=old[x:]
    c=open(head+'副本'+kuozhan,'w')
    while True:
        b=a.read(2)
        print(b)
        if len(b) == 0:
            break
        c.write(b)
    a.close
    c.close
n=input('请输入源文件名称: ')
myself(n)
