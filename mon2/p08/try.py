try:
    a=open(input('请输入文件名称: '),'r')
    print(a.read())
except FileNotFoundError:
    print('抓住了')
else:
    print('没有异常')
