# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# 0,56 -> 11

def summ (value):
    summ = 0
    while value > 0:
        summ = summ + value %10
        value //= 10
    return summ

n = (input('Введите число: '))
res = n.split(',')
left_part = int(res[0])
right_part = int(res[1])
print(f'сумма цифр введенного числа = {summ(left_part) + summ(right_part)}')

