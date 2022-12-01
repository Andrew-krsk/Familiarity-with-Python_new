# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

# ['213213', 'dsf653', 'dsf', 'fdh76']
# num = 3
# Вывод: '213213', 'dsf653'



def find_num(list: list[str], num: str):
    for i in range(len(list)):
        if num in list[i]:
            print(list[i])


list = ['213213', 'dsf653', 'dsf', 'fdh76']
num = input('Введите искомое значение: ')

find_num(list, num)
