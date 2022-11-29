# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.
# 'Я люблю Python'
# 'лю'
# 2

# text_1 = input("Введите строку 1: ")
# text_2 = input("Введите строку 2: ")

# count = 0
# for i in range(0, len(text_1)-1):
#     if text_1[i] + text_1[i + 1] == text_2:
#         count += 1
# print(count)


# s1 = input()
# s2 = input()
# print(s1.count(s2))

# s1 = 'ЯлюблюлюблюлюблюPython'
# s2 = 'люблю'
# i = 0
# cnt = 0
# while i < len(s1) - 1:
#     if s1[i:len(s2) + i] == s2:
#         cnt += 1
#     i += 1
# print(cnt)

# s1 = 'ЯлюблюлюблюлюблюPython'
# s2 = 'лю'
# cnt = 0
# while s2 in s1:
#     s1 = s1.replace(s2, ' ', 1)
#     print(s1)
#     cnt += 1
# print(cnt)

# s1 = 'Я люблю люблюлюблюPython'
# s2 = 'лю'
# res = s1.split(s2)
# print(res)
# print(len(res) - 1)