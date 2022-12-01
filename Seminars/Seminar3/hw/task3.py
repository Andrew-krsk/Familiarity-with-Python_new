# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 10.01] => 0.19

def fill_list(n: int) -> list[float]:
    list = []
    for i in range(n):
        list.append(float(input(f'Введите {i+1} элемент списка: ')))
    return list

def only_float_parts(list: list[float]) -> list[float]:
    new_list = []
    for i in range(len(list)):
        new_list.append(round(list[i]%1, 2))
    return new_list

n = int(input('Введите количество значений в списке: '))
list = fill_list(n)
res = max(only_float_parts(list)) - min(only_float_parts(list))
print(f'{list}, => {res}')