def aa():
    print("*"*50)
def aaa(a):
    s=a+a
    print(s)
def aaaa(a,b):
    print(a,b)
def b(*s):
    b=0
    for i in s:
        b=b+i
    print(s)
    print(b)
sb=20
bd=["BC","ABC","ICBC",999]
c={"一刀":999,"皇城PK":"贪玩蓝月"}
aa()
aaa(sb)
aaaa(sb,bd)
vx=2
b(vx,sb,28)

