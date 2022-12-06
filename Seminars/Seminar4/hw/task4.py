# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.

import random

def write_to_file(st: str):
    with open('file_sem4_hw4.txt', 'w') as data:
        data.write(st)

def rnd():
    return random.randint(0,10)

def create_list(k: int) -> list [int]:
    list = [rnd() for i in range(k+1)]
    return list
    
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

k = int(input("Введите натуральную степень k = "))
list = create_list(k)
write_to_file(create_st(list))
