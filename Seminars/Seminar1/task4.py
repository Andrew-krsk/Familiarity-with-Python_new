# Напишите программу, которая будет принимать на вход дробь и показывать певую цифру дробной части числа
# пример:
# 6,78 -> 7
# 0,34 -> 3

# n = input('введите число: ')
# print(n[2])


# n = float(input('введите число: '))
# a = (n*10)%10
# print(int(a))

string = input('введите число: ').split(',')[1][0]
print(string)