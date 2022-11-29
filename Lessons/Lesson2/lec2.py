# Запись данных в файл:

# Враинат 1:

# colors = ['red', 'green', 'blue123']
# data = open('file.txt', 'a')
# # data.writelines(colors)     #разделителей не будет
# data.write('LINE 12\n')
# data.write('LINE 13\n')
# data.close()

# Вариант 2:
# with open('file.txt', 'a') as data:
#     data.write('line 111456\n')
#     data.write('line 222465\n')


# Чтение данных из файла (вывод в терминал):

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()



# Методы:

# def function_name(x):
    # body line 1
    # ...
    # body line n
    # optional return

# import hello             # Название файла из которого хотим импортировать функцию

# print(hello.f(1))       # Название файла.функция(аргумент) 

import hello as h             # Название файла из которого хотим импортировать функцию или 
                                # применить к этому файлу новое имя, которое будем дальше использовать в этом файле

# print(h.f(1))           # Название файла.функция(аргумент) 

# Пример 1:
# def new_string(symbol, count):
#     return symbol * count

# print(new_string('!', 5))       # !!!!!
# print(new_string('!'))          # TypeError missing 1 required ...


# Пример 2:
# def new_string(symbol, count = 3):
#     return symbol * count

# print(new_string('!', 5))       # !!!!!
# print(new_string('!'))          # !!!
# print(new_string(4))            # 12


# Возможность передачи неограничеенного количества аргументов

# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a', 's', 'd', 'w'))     # asdw
# print(concatenatio('a', '1', 'd', '2'))     # a1d2
# print(concatenatio(1, 2, 3, 4))             # TypeError: ...


# Рекурсия

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)                     # 1 1 2 3 5 8 13 21 34




# Кортежи:
# Кортеж - неизменяемый список

# a = (3, 4)
# print(a)
# print(a[0])         # Обращение к конкретному элементу кортежа
# print(a[-1])         # Обращение к последнему элементу кортежа
# print(a[-2])         # Обращение ко 2му элементу кортежа с конца

# a = (3, 4, 5)
# for item in a:
#     print(item)

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))





# Словари:
# Реупорядоченные коллекции произвольных объектов с доступом по ключу:

# dictionary = {}
# dictionary = \
#     {
#         'up': 'вверх',
#         'left': 'влево',
#         'down': 'вниз',
#         'right': 'вправо'
#     }

# print(dictionary)
# print(dictionary['left'])

# for k in dictionary.keys():         # Посмотреть все ключи в словаре
#     print(k)


# for k in dictionary.values():         # Посмотреть все значения в словаре
#     print(k)





# Множества:


# Неупорядоченная совокупность элементов


# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a)) # set
# print(type(b)) # set

# b = set([2, 5, 8, 13, 21])
# c = set((2, 5, 8, 13, 21))
# print(type(a)) # set
# print(type(b)) # set
# print(type(c)) # set
# a = {1, 1, 1, 1, 1}
# print(a) # {1}

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a \
#  .union(b) \
#  .difference(a.intersection(b))
# # {1, 21, 3, 13}


# Неизменяемое множество
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})


# Списки:

list1 = [1,2,3,4,5]
# print(list1)
# print(list1.pop())          # Удаление последнего элемента списка
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)


# print(list1.pop(2))            # Удаление конкретного элемента списка по индексу

# print(list1.insert(2, 11))      # Добавление конкретного элемента списка по индексу
# print(list1)

# print(list1.append(11))      # Добавление конкретного элемента списка в конец списка
# print(list1)

