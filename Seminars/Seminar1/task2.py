# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них
# Примеры:
# -1, 4, 8, 7, 5 -> 8
# 78, 55, 36, 90, 2 -> 90

# a, b, c, d, e = int(input('введите число 1: ')), int(input('введите число 2: ')), int(input('введите число 3: ')), int(input('введите число 4: ')), int(input('введите число 5: '))
# print(f'max = {max(a, b, c, d, e)}')


# num = 0
# maxx = 0

# for _ in range(5):
#     num = int(input('Введите число: '))
#     if num > maxx:
#         maxx = num
# print(maxx)

# range(5) -> 0, 1, 2, 3, 4
# range(1, 4) -> 1, 2, 3
# range(1, 10, 2) -> 1, 3, 5, 7, 9


# array = []
# for i in range(5):
#     array.append(int(input('Введите число: ')))
# max_count = max(array)
# print(array)
# print(max_count)


# from random import randint

# array = []
# for i in range(5):
#     array.append(randint(-10, 10))      # от -10 до 10 включительно
# max_count = max(array)
# print(array)
# print(max_count)


# Срезы:

# a = [42, 67, 12, 87, 112]

# a[1:3] -> [67, 12]
# a[2:] -> [12, 87, 112]
# a[::2] -> [42, 12, 112]
