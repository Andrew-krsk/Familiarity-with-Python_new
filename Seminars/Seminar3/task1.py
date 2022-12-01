# Реализуйте алгоритм задания случайных чисел без использования втроенного генератора псевдослучайных числел

# import time

# def rand(num):
#     return int(round(time.time() %1, 1) * 10)

# print(rand(4))



# def rand(start_num: int=1, finish_num=1) -> int:
#     while True:
#         num = int(round(time.time() %1, 1) * 10)
#         if start_num <= num <= finish_num:
#             return num

# print(rand(10, 45))



from datetime import datetime

def rand(n: int) -> int:
    now = datetime.now()
    rand_num = now.time().second ** now.time().minute * now.time().microsecond
    return rand_num % 10**n

print(rand(3)) 