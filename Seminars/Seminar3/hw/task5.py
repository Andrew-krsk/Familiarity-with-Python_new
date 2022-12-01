# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def negafib(k: int) -> list[int]:
    list = [1, 1]
    for i in range(2, k):
        list.append(list[i-2] + list[i-1])
    for i in range(k+1):
        list.insert(0, list[1] - list[0])
    return list


k = int(input('Введите число: '))
print(f'для k = {k} последовательность = {negafib(k)}')
