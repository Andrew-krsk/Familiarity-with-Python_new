# Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]


def orig_num(list: list [int]) -> list [int]:
    lst_out = []
    for j in list:
        count = 0
        for i in list:
            if j == i:
                count += 1
        if count < 2:
            lst_out.append(j)
    return lst_out


list = [1, 1, 2, 3, 4, 4, 4, 5]
print(orig_num(list))

