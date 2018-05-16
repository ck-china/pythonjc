a=[]
while True:
    name=input('输入名字,输入q来退出')
    if name == "q":
        break
    a.append(name)
print("列表",a)
print(a[3])
print(a[5])
print(a[8])
print(a[10])
a.sort
print("正序",a)
a.sort(reverse=True)
a.reverse
print("倒序",a)
a.pop
print("弹出最后以为同学",a)
del a[2]
a1=["张三","李四","王麻子"]
print(a1)
a.extend(a1)
print(a)
b=a.index("小明")
print("小明所在的位置是：",b)
