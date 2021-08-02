def zarb(x):
    print(x * 3)

zarb(2)

def zarb1(x,y):
    return x * y
res = zarb1(3, 3)
print(res)

def zarb2(x,y):
    return (x*y , x*2 , y*3)
res2 = zarb2(5, 7)
print(res2)

def zarb3(x,y):
    return (x*y , x*2 , y*3)
res2,x2,y3 = zarb3(5, 7)
print(res2)
print(x2)
print(y3)
