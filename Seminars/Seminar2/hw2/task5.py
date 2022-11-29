# Реализуйте алгоритм перемешивания списка.

import random
from random import randint

list = []
for i in range(10):
    list.append(randint(-10, 11))

print(list)

for i in range(len(list)-1):
    rand_index = randint(0, len(list)-1)
    temp = list[i]
    list[i] = list[rand_index]
    list[rand_index] = temp

print(list)


# random.shuffle(list)  
# print(list)
