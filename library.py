import random

print(dir(random))
print(random.choice('ali rahimi'))
print(random.randint(0, 33))
print(random.random())
print('finish random\n')


import time

print(dir(time))
print(time.time())
print(time.gmtime(time.time()))

print('finish time\n')

print('ali')
time.sleep(3)
print('rahimi')
print('finish sleep\n')

import winsound , random

winsound.Beep(800,1000)
f = random.randint(800, 2000)
d = random.randint(1000, 3000)

winsound.Beep(f , d)
print('finish winso')

import winsound , random , time

time.sleep(3)
while 1:

    a = random.randint(800, 20000)
    b = random.randint(100, 300)

    winsound.Beep(a , b)
print('finish winso 2')