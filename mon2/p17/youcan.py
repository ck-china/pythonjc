def wai(f):
    def nei(*a):
        print("--==--执行前的检查--==--")
        f(a)
    return nei
@wai
def foo(*it,**its):
    print('foo 正在执行')
    print("传的参数是 %s"%it)
    print("传的参数是 ",its)
foo('哈马批','小赤佬',ss:666,bb:2)
