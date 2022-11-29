# # Переменные

# value = None
# # print(type(value))
# # print(type(a))
# # print(type(b))
# # print(type(value))

# value = 132456
# a = 123
# b = 1.23
# s = 'hello world'

# # Способы вывода:

# print(a, '-', b, '-', s)
# print('{} - {} - {}'.format(a, b, s))
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')   # Интерполяция

# # Логическая переменная

# f = False # или True
# print(f)

# # Списки

# list = [1, 2, 3] # список целочисленных значений
# list = ['1', '2', '3', 'hello world'] # список строк
# list = ['1', '2', '3', 'hello world', 1, 2, 4.5, True] # список любых типов данных в одном списке 
#                                                        # (Лучше создавать списки с определенным типом данных)

# list = ['1', '2', '3']
# col = ['hello world', 1, 2, 4.5, True]

# # print(list)
# # print(col)

# Ввод и вывод данных:

# print('Введите a')
# a = float(input())
# print('Вевдите b')
# b = float(input())
# print(a, '+', b, '=', a+b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# Арифметические операции:

# a = +123 # унарный плюс, в программировании моет быть написан
# b = -321
# c = a + b
# print(c)

# a = 2
# b = 8
# c = a - b
# print(c)

# a = 2
# b = 8
# c = a * b
# print(c)

# a = 12
# b = 8
# c = a / b
# print(c)

# a = 12 # Деление в целых числах
# b = 8
# c = a // b
# print(c)

# a = 12 # Остаток от деления
# b = 8
# c = a % b
# print(c)

# a = 2 # Возведение в степень
# b = 8
# c = a ** b
# print(c)

# a = 1.35131354 # Количество знаков после запятой в результате
# b = 3
# c = round(a * b, 5)
# print(c)

# # Операции присваивания:
# a = 3
# a = a + 5 # аналогично a += 5, a *= 5
# print(a)

# Логические операции:

# a = 1 > 4 # True или False
# print(a) 

# a = 1 < 4 and 5 > 2  # True или False
# print(a) 

# a = 1 == 2  # True или False  Сравнение
# print(a) 

# a = 1 != 2  # True или False    Неравенство
# print(a) 

# Можно сравнивать строки и списки
# a = 'qwe'
# b = 'qwe'
# print(a == b)

# a = [1, 2]
# b = [1, 2]
# print(a == b)

# Можно использовать тройные или четверные неравенства

# a = 1 < 3 < 5 < 10
# print(a)

# f = 1 > 2 or 4 < 6 # или
# print(f)

# f = [1, 2, 3, 4]
# print(f)
# print(2 in f) # True потому что 2 есть в этом списке f

# f = [1, 2, 3, 4]
# print(f)
# print(not 2 in f) # False (not - отрицание)

# f = [1, 2, 3, 4]
# # print(f)
# # print(not 2 in f) # False (not - отрицание)

# # is_odd = f[0] % 2 == 0 # False, число нечетное
# # print(is_odd)

# is_odd = not f[0] % 2 # False, потому что отрицание 1 это 0 а это ложь
# print(is_odd)

# Управляющие конструкции if, if-else

# if condition:
#     # operator 1
#     # operator 2
#     # ...
#     # operator n
# else:
#     # onerator n + 1
#     # onerator n + 1
#     # ...
#     # onerator n + m

# Пример:
# a = int(input('Введите число а > '))
# b = int(input('Введите число b > '))
# if a > b:
#     print(a)
# else:
#     print(b)



# if condition 1:
#     operator
# elif condition 2:
#     operator
# elif cindition 3:
#     operator
# else:
#     operator

# Пример:
# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же Маша!')
# elif username == 'Марина':
#     print('Я так ждал вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Привет,', username)


# Опреатор While:
# while condition:
#     operator 1
#     operator 2
#     ...
#     operator n

# Пимер:
# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# While + else
# while condition:
#     operator 1
#     operator 2
#     ...
#     operator n
# else:
#     # onerator n + 1
#     # onerator n + 1
#     # ...
#     # onerator n + m

# Пример
# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('пожалуй')
#     print('хватит )')
# print(inverted)


# For
# for i in enumeration:
#     operator 1
#     operator 2
#     ...
#     operator n

# Пример:
# for i in 1, 2, 3, 4, 5:
#     print(i**2)

# list = [1, 2, 3, 10, 5]
# for i in list:
#     print(i)

# r = range(10)
# for i in r:
#     print(i)

# for i in range(5):
#     print(i)

# for i in range(1, 4):
#     print(i)

# for i in range(1, 10, 2):
#     print(i)

# for i in 'qwerty':
#     print(i)

# Работа со строками:
# text = 'съешь еще этих мягких французских булок'
# print(len(text))            #39
# print('еще' in text)        #True
# print(text.isdigit())       #False
# print(text.islower())       #True
# print(text.replace('еще','ЕЩЕ'))   


# text = 'съешь еще этих мягких французских булок'
# print(text[0])                  #c
# print(text[len(text)-1])        #k обращение к последнему элементу строки
# print(text[-5])                 #б обращение к 5 элементу строки с конца
# print(text[:])                  # Печать всего текста
# print(text[:2])                 #съ печать символово от 0го до 2го(не включая)
# print(text[len(text)-2:])       #ok печать символов от 2 с конца до последнего
# print(text[6:9])                #еще печать символов от 6 до 9
# print(text[0:len(text):6])      #сеикакл печатает каждую 6 символ от начала до конца
# print(text[::6])                #сеикакл тоже самое только в другой записи


# Списки

# numbers = [1, 2, 3, 4, 5]
# print(numbers)

# ran = range(1, 6)               # последний элемент не включительно
# numbers = list(ran)
# print(numbers)
# # print(len(numbers))             #5

# for i in numbers:
#     i *= 2
#     print(i)
# print(numbers)

colors = ['red', 'green', 'blue']
for e in colors:
    print(e)

for e in colors:
    print(e*2)

colors.append('gray')
print(colors)

colors.remove('red')
print(colors)

del colors[0]
print(colors)

# Функции

# def function_name(x):
#     body line 1
#     ...
#     body line n
#     optional return

# Пример:
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23   
    else:
        return

arg = 2
print(f(arg))
print(type(f(arg)))
