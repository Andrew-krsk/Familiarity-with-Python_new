# LAMBDA + LIST COMPREHENSION
# 
# 
# Вариант 1:
# path = 'file_les3_task4.txt'
# f = open(path, 'r')
# data = f.read() + ' '
# f.close

# numbs = []

# while data != '':
#     space_pos = data.index(' ')
#     numbs.append(int(data[:space_pos]))
#     data = data[space_pos+1:]

# out = []
# for e in numbs:
#     if not e % 2:
#         out.append((e, e**2))

# print(out)



# Вариант 2:
# def f(x):
#     return x**2

# list = [(i, f(i)) for i in list if (i%2 == 0)]
# print(list)



# # Вариант 3:
# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()

# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = select(lambda x:(x, x**2), res)
# print(res)