# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# 
# Пример:
# 
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

n = int(input('Введите число n: '))
list_n = [i for i in range(-n, n + 1)]
# for i in range(-n, n + 1):
#     list_n.append(i)
    
m = input('Введите номера индексов одной строкой через пробел: ')
res = m.split(" ")
list_m = [int(i) for i in res]

multi = 1
for i in range(len(list_m)):
    multi *= list_n[list_m[i]]

print(list_n)
print(list_m)
print(f'Вывод: {multi}')