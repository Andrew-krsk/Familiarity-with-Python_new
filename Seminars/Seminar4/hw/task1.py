# Вычислить число c заданной точностью d

# Пример:

# - при d = 0.001, π = 3.141   
# Ввод: 0.01
#     Вывод: 3.14

#     Ввод: 0.001
#     Вывод: 3.141

import math

d = float(input('Введите точность d (пример 0.01, 0.001...): '))
pi = math.pi

d = str(d)
d = d.split('.')
d_acc = d[1]
count = 0
for i in d_acc:
    count += 1

print(round(pi, count))