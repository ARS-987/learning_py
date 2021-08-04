def func(a , b=333):
    print("a = " , str(a) , "\nb = " , str(b))
func(3)
print('finish1')
func(3,33)
print('finish2')
def func1(x , *tuple):
    print("x = " , str(x) , '\ntuple = ' , str(tuple))

func1(3,4,5,7,8)
print('finish3')
