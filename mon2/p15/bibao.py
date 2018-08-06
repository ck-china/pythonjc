def test(out):
    def test1(li):
        print("里面的是%d"%li)
        return out+li
    return test1
n=test(1)(2)
print(n)
