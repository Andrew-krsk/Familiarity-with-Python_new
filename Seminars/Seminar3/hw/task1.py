# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

import random

# def fill_list(n: int) -> list[int]:
#     list = []
#     for i in range(n):
#         list.append(int(input(f'Введите {i+1} элемент списка: ')))
#     return list

# def summ_of_odd_el(list: list) -> int:
#     summ = 0
#     for i in range(1, len(list), 2):
#         summ += list[i]
#     return summ

# n = int(input('Введите количество значений в списке: '))
# # print(f'Сумма элементов списка, стоящих на нечётной идексах = {summ_of_odd_el(fill_list(n))}')

# lst = [random.randint(1, 10) for i in range(1, n, 2)]
# print(lst)
# print(sum(lst))

