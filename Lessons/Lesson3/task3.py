# list = []

# for i in range(1, 101):
#     # if (i%2 == 0):
#         list.append(i)

# print(list)


# Упрощенное создание списка:
# list = [i for i in range(1, 21) if (i%2 == 0)]
# print(list)



# Сделать список кортежей:
# list = [(i, i) for i in range(1, 21) if (i%2 == 0)]
# print(list)


# Использование функции при создании списка:
def f(x):
    return x**3

list = [f(i) for i in range(1, 21) if (i%2 == 0)]
print(list)