
# ПРИМЕНЕНИЕ LIST COMPREHENSION И ВСТРОЕННЫХ ФУНКЦИЙ
# ПРИМЕНЕНИЕ LAMBDA


# ВАРИАНТ 1


# import functools

# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

# Пример:

# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

# list = []
# n = int(input('Введите число n: '))
# # for i in range(1,n+1):                                # БЫЛО
# #     a=(1 + 1/i)**i
# #     list.append(a)
# list = [((1 + 1/i)**i) for i in range(1,n+1)]           # СТАЛО (LIST COMPREHENSION)

# # summ = 0                                              # БЫЛО
# # for i in range(n):
# #     summ = summ + list[i]
# # summ = sum(list)                                      # СТАЛО_1 (ВСТРОЕННАЯ ФУНКЦИЯ(SUM))
# summ = functools.reduce((lambda x, y: x + y), list)     # СТАЛО_2 (LAMBDA И functools.reduce)
# print(f'Сумма всех чисел = {round(summ, 2)}')



# =========================

# ВАРИАНТ 2

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

import random

# def fill_list(n: int) -> list[int]:                                                               # БЫЛО
#     list = []
#     for i in range(n):
#         list.append(int(input(f'Введите {i+1} элемент списка: ')))
#     return list

# def summ_of_odd_el(list: list) -> int:
#     summ = 0
#     for i in range(1, len(list), 2):
#         summ += list[i]
#     return summ

n = int(input('Введите количество значений в списке: '))
# print(f'Сумма элементов списка, стоящих на нечётной идексах = {summ_of_odd_el(fill_list(n))}')

lst = [random.randint(1, 10) for i in range(1, n, 2)]                                               # СТАЛО (LIST COMPREHENSION)
print(sum(lst))