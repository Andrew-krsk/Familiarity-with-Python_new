# def f(x):
#     x**2

# g = f
# print(f(1))
# print(g(1))


def calc(x):
    return x+10

print(calc(10))


def calc_2(x):
    return x*10

print(calc_2(10))


def math(op, x):
    print(op(x))

math(calc_2, 10)
math(calc, 10)