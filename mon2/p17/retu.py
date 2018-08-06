def wai(f):
    def nei():
        print('_____啦啦啦_____')
        return (f())
    return nei
@wai
def foo():
    return '火锅底料'
print(foo())

