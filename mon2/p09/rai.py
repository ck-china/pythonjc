class test(object):
    def __init__(self):
        self.swi="open"
    def div(self,a,b):
        try:
            return a/b
        except Exception as res:
            if self.swi == 'open':
                print('抓住异常, %s'%res)
            else:
                raise
xx=test()
xx.div(9,0)
