# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def convert_to_binary(n) -> list[str]:
    list = []
    while n > 1:
        if n%2 == 0:
            list.insert(0, '0')
        else:
            list.insert(0, '1')
        n //= 2
    list.insert(0, '1')
    return list


n = int(input('Введите значение десятичного числа: '))
list = convert_to_binary(n)
print(f'{n} -> ', end='')

for i in range(len(list)):
    print(list[i], end='')

