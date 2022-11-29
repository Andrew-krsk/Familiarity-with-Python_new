# Напишите программу, которая на вход принимает число N и выводит числа от -N до N 
# Пример:
# -5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

N = int(input('Введите число N: '))
for item in range(-N, N + 1):
    print(f'{item}', end=' ')


# n = int(input('введите число: '))
# numbers = []

# for i in range(-n, n + 1):
#     numbers.append(i)
# print(numbers)
