# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ⋀ - and
# ⋁ - or
# ¬ - not

x = input('Введите x: ')
y = input('Введите y: ')
z = input('Введите z: ')

left_part = not (x or y or z)
right_part = not x and not y and not z
if left_part == right_part:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')