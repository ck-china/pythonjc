import time
while True:
    import random
    a=random.randint(1,110)
    if a%2==0:
        print(" "*a,"$")
    else:
        print(" "*a,"￥")
    time.sleep(0.3)
