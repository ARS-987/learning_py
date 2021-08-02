str = input('enter full name: ')
res = ''
for i in str:
    if i.isalpha():
        if i.isupper():
            res += i.lower()
        else:
            res += i.upper()
    else:
        res += i
print(str)
print(res)


print('Ali\tRahimi Sadegh\nKerman')