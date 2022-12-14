# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов (складываются числа, у которых "х" в одинаковых степенях). 
# Пример того, что будет в итогвом файле: 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0

import random

# запись в файл
def write_file(name: str, st: str):
    with open(name, 'w') as data:
        data.write(st)

# создание коэффициентов многочлена
def create_list_of_koef(k: int) -> list[int]:
    list = [random.randint(1, 9) for i in range(k+1)]
    return list
    
# создание многочлена в виде строки 
def create_st(list: list[int]) -> str:
    st = ''
    if len(list) < 1:
        st = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and i != len(list) - 2 and list[i] != 0 :
                st += f'{list[i]}x^{len(list)-i-1}'
                if list[i+1] != 0:
                    st += ' + '
                if list[i+1] == 0 and i+1 != len(list) - 1 and i+1 != len(list) - 2:
                    st += ' + '
            elif i == len(list) - 2 and list[i] != 0:
                st += f'{list[i]}x'
                if list[i+1] != 0:
                    st += ' + '
            elif i == len(list) - 1 and list[i] != 0:
                st += f'{list[i]} = 0'
            elif i == len(list) - 1 and list[i] == 0:
                st += ' = 0'
    return st

# получение степени многочлена
def degree_str_to_int(k) -> int:
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num

# получение коэффицента члена многочлена
def koef_str_to_int(k) -> int:
    if 'x' in k:
        i = k.find('x')
        num = int(k[i-1])
    return num

# разбор многочлена и получение его коэффициентов
def list_of_koef_int(st: str) -> list[int]:
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    length = len(st)
    if degree_str_to_int(st[-1]) == -1:
        lst.insert(0, int(st[-1]))

        # Создать словарь и добавить значение degree_str_to_int[-1] : степень 0

        length -= 1
    degree = 1 # степень
    index = length-1 # индекс
    while index >= 0:
        if degree_str_to_int(st[index]) != -1 and degree_str_to_int(st[index]) == degree:
            lst.insert(0, koef_str_to_int(st[index]))

            # Добавление значения в словарь degree_str_to_int(st[index]) : степень index

            index -= 1
            degree += 1
        else:
            lst.insert(0, 0)
            degree += 1

            # Добавление значения в словарь значение 0 : степень index

    print(lst)
    return lst
    
# создание двух файлов

k1 = int(input("Введите натуральную степень для первого файла k = "))
k2 = int(input("Введите натуральную степень для второго файла k = "))
list_of_koef1 = create_list_of_koef(k1)
list_of_koef2 = create_list_of_koef(k2)
write_file("file_sem4_hw5_1.txt", create_st(list_of_koef1))
write_file("file_sem4_hw5_2.txt", create_st(list_of_koef2))

# нахождение суммы многочлена

with open('file_sem4_hw5_1.txt', 'r') as data:
    st1 = data.readlines()
with open('file_sem4_hw5_2.txt', 'r') as data:
    st2 = data.readlines()

print(f'Первый многочлен {st1}')
print(f'Второй многочлен {st2}')

lst1 = list_of_koef_int(st1)
lst2 = list_of_koef_int(st2)
length = len(lst1)
if len(lst1) > len(lst2):
    length = len(lst2) # length = какое больше (len(lst1) или (len(lst2)))
    
# Из 2 словарей создать 2 списка со значениями по индексам и сложить их

lst_new = [lst1[i] + lst2[i] for i in range(length)]

if len(lst1) > len(lst2):
    mm = len(lst1)
    for i in range(length,mm):
        lst_new.append(lst1[i])
else:
    mm = len(lst2)
    for i in range(length,mm):
        lst_new.append(lst2[i])
        
write_file("file_sem4_hw5_res.txt", create_st(lst_new))
with open('file_sem4_hw5_res.txt', 'r') as data:
    st3 = data.readlines()
print(f"Результирующий многочлен {st3}")