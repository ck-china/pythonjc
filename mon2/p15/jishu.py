def jishu(a):
    n=0
    while n < a:
        if n % 2 != 0:
            yield(n)
        n+=1
a=jishu(100)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
