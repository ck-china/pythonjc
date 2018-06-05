import os
def shanchu(name):
    os.remove(name)
print('删除函数')
shanchu(input('请输入要删除的文件名称：'))
def gaiming(name,name2):
    os.rename(name,name2)
print('改名函数')
ss=input('请输入新文件名称：')
gaiming(input('请输入源文件名称：'),ss)
print('新文件的名称是:%s'%ss)
