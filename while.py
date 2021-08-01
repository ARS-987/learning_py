x = 100
while x>=0:
    print (x)
    x -= 10
print ('finish')


z = 100
while z >= 0:
    z -= 3
    if z <=30:
        break
    print (z)
print ('finish')

y = 10 
while y>=0:
    y -= 1
    if y == 5:
        continue
    if y == 0:
        break
    print (y)
print ('finish')


while True:
    a = int(input())
    if a % 2 == 0:
        break
print ('Error')