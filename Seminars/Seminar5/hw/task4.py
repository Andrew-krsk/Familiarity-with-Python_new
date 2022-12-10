# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


def create_lst(data):
    lst = []
    lst.append(data.count('a'))
    lst.append('a')
    lst.append(data.count('b'))
    lst.append('b')
    lst.append(data.count('c'))
    lst.append('c')
    return lst


path = 'file_seminar5_hw_task4.txt'
f = open(path, 'r')
data = f.read()
f.close

lst = list(map(str, create_lst(data)))
st = ''.join(lst)

with open('file_seminar5_hw_task4_result.txt', 'w') as file:
        file.write(st)