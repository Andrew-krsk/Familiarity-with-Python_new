# # Напишите программу, удаляющую из текста все слова, содержащие "абв".
# --> 'Я люблю абвЖвау иабв Питон'
# --> 'Я люблю Питон'
# # включений, filter, map



s = 'Я люблю абвЖвау иабв Питон'
res = [i for i in s.split() if 'абв' not in i]
print(res)






