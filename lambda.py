def sum(a ,b):
    return a+b
print(sum(3,5))

print('\n')

sum = lambda a,b:a+b
print(sum(4,9))

print('finish')


def plus7(list):
    res = []
    for i in list:
        res.append(i+7)
    return res
lis = [3,5,6,8,90]
new_list = plus7(lis)
print(new_list)

print('\n')

list1 = [3,5,6,8,90]
new_list1 = list(map(lambda i:i+7, list1))
print(new_list1)

print('finish1')