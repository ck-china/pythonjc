'''
def fib(day):
    n=0
    a,b=0,1
    while n < day:
        yield(b)
        a,b=b,a+b
        n += 1
f=fib(10)
print(next(f))
print(next(f))
print(next(f))
'''
for i in range(1,101):
    for y in (1,i+1):
        if i % y == 0:
            print(i)
