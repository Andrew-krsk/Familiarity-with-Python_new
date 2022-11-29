# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

# Пример:

# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

list=[]
n = int(input('Введите число n: '))
for i in range(1,n+1):
    a=(1 + 1/i)**i
    list.append(a)

summ = 0
for i in range(n):
    summ = summ + list[i]

print(f'Сумма всех чисел = {round(summ, 2)}')