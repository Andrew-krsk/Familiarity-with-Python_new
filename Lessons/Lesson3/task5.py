# MAP

# Вариант 1:

# li = [x for x in range(1, 20)]

# li = list(map(lambda x: x + 10, li))
# print(li)




# Вариант 2:

# data = list(map(int, '1 2 3'.split()))

# for e in data:
#     print(e)

# print('--')

# for e in data:
#     print(e)




# Вариант 3:

def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()

res = map(int, data)
res = where(lambda x: not x % 2, res)
res = list(map(lambda x:(x, x**2), res))
print(res)