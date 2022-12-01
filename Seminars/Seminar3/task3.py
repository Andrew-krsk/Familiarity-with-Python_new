# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что ее нет:

# Пример:
# ['qwe', 'asd', 'xzc', 'qwe', 'ertqwe'],         ищем 'qwe', ответ: 3
# ['йцу', 'фыв', 'ячс', 'цук', 'йцукен', 'йцу']   ищем 'йцу', ответ: 5
# ['йцу', 'фыв', 'ячс', 'цук', 'йцукен']          ищем 'йцу', ответ: -1
# ['123', '234', 123, '567']                      ищем '123', ответ: -1 (isinstance)
# []                                              ищем '123', ответ: -1


def find_string(list: list, str) -> int:
    count = 0
    for i in range(len(list)):
        if str == list[i]:
            count += 1
            if count == 2:
                return i
    return -1        

list = ['qwe', 'asd', 'xzc', 'qwe', 'ertqwe']
str = input('Введите искомую строку: ')
print(find_string(list, str))