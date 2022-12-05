# FILTER

data = [x for x in range(10)]

res = list(filter(lambda x: not x % 2, data))

print(res)



# Вариант 2:

# data = '1 2 3 5 8 15 23 38'.split()

# res = map(int, data)
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x:(x, x**2), res))
# print(res)