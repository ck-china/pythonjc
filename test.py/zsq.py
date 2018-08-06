def wai(a):
    def nei():
        print('yanzheng')
        a()
    return nei
@wai
def fi():
    print('hhh')
fi()
