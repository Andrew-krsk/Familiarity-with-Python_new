
# ПРИМЕНЕНИЕ MAP
# ПРИМЕНЕНИЕ LAMBDA


# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 10.01] => 0.19

def fill_list(n: int) -> list[float]:
    lst = []
    for i in range(n):
        lst.append(float(input(f'Введите {i+1} элемент списка: ')))
    return lst

def only_float_parts(lst: list[float]) -> list[float]:                          
    new_list = list(map(lambda x: round(x %1, 2), lst))                         # СТАЛО (MAP, LAMBDA)
    # for i in range(len(list)):                                                # БЫЛО
    #     new_list.append(round(list[i]%1, 2))
    return new_list

n = int(input('Введите количество значений в списке: '))
lst = fill_list(n)
# print(only_float_parts(lst))
res = max(only_float_parts(lst)) - min(only_float_parts(lst))
print(f'{lst}, => {res}')

# Куда прикрутить ZIP, Enumerate и Filter, так чтобы это было логично и обосновано, так и не придумал. 
# Думаю где-то встретится дальше


