def zsq(a):
    def wai(f):
        def nei():
            print('++++例行检查++++')
            print('最外层的使用',a)
            return (f())
        return nei
    return wai
@zsq('火锅底料')
def foo():
    return ('红油')
print(foo())
