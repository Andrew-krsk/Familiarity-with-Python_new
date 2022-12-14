# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
    
#     1) с помощью математических формул нахождения корней квадратного уравнения
#     2) с помощью дополнительных библиотек Python (scipy)

def kv(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return 'Корней нет'
    if d == 0:
        return -(b / 2 * a)
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    return x1, x2


print(kv(1, 1, -3))

