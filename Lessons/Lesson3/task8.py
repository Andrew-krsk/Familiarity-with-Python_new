# ENUMERATE


# # Вариант 1:
# users = ['user1', 'user2', 'user3', 'user4', 'user5']

# data = list(enumerate(users))

# print(data)

# Вариант 2:
# Если необходимо проеумеровать с 1, то вторым аргументом передаем с какого номера начинать
users = ['user1', 'user2', 'user3', 'user4', 'user5']

data = list(enumerate(users, 1))

print(data)


