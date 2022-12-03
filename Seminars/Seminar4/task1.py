# # Чтение данных из файла (вывод в терминал):

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()


# Считать строку набора чисел из файла. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел. Результат запишите в исодный файл (minn maxx).

import random

with open('file_sem1_task1.txt', 'w') as f:
    for i in range(500):
        f.write(str(random.randint(1, 10000)) + '\n')
        

with open('file_sem1_task1.txt', 'r') as f:
    sp = [int(x) for x in f.readlines()]
print(min(sp), max(sp))


