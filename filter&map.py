num = [2,4,5,6,9, 10,23,33,90]

def plus5(n):
    return n+5
n_l = []
for i in num:
    n_l.append(plus5(i))
print(n_l)

n_l2 = list(map(plus5, num))
print(n_l2)

n_l3 = list(map(lambda i : i+5, num))
print(n_l3)

print('finish map')

def more_than_10(n):
    if n > 10:
        return True
    else:
        return False
n_l4 = list(filter(more_than_10, num))
print(n_l4)

n_l5 = tuple(filter(lambda n : n >= 10,num))
print(n_l5)