# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def fill_list(n: int) -> list[int]:
    list = []
    for i in range(n):
        list.append(int(input(f'Введите {i+1} элемент списка: ')))
    return list

def multi_of_pairs(list: list, k: int) -> list[int]:
    if k % 2 == 0:
        k = len(list)
    else:
        k = len(list) + 1
    multi = []
    for i in range(k//2):
        multi.append(list[i] * list[-i-1])
    return multi


n = int(input('Введите количество значений в списке: '))
list = fill_list(n)
multi = multi_of_pairs(list, len(list))
print(f'{list}, => {multi}')
