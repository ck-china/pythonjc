import random
import time
print('今天抽三位幸运儿拿来烧广东煲仔汤')
time.sleep(1)
print('谁会这么幸运呢')
time.sleep(1)
print('已经选好了列')
time.sleep(2)
print('正在选择行')
time.sleep(2)
print('已经选好了行')
time.sleep(2)
print('掌声送给他们')
time.sleep(1)
print('他们是:')
time.sleep(3)
a=1
while a <=3:
    b=random.randint(1,7)
    c=random.randint(1,6)
    print('%d列%d行的同学'%(b,c))
    a+=1
    time.sleep(1)
