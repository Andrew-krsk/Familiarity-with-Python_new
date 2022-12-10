# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# Чтобы победить в этой игре, первым ходом игороку необходимо взять:
# Общее количество конфет % максимальное кол-во конфет за один ход + 1,
# а затем, каждым своим ходом добавлять конфет до максимального кол-ва конфет за один ход + 1

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

import random

# Игра PvP

def lottery() -> list[int]:
    n = random.randint(1, 2)
    lst = []
    if n == 1:
        lst = [1, 2]
    else:
        lst = [2, 1]
    return lst

def game_PvP(candies: int, lst: list[int]):
    while candies > 0:
        n = int(input(f'Игрок {lst[0]} ваш ход. Напишите сколько конфет вы возьмете (от 1 до 28): '))
        candies -= n
        if candies > 0:
            print(f'Остаток конфет {candies}')
        if candies <= 0:
            print(f'Игра окончена. Игрок {lst[0]} победил')
            break
        n = int(input(f'Игрок {lst[1]} ваш ход. Напишите сколько конфет вы возьмете (от 1 до 28): '))
        candies -= n
        if candies > 0:
            print(f'Остаток конфет {candies}')
        if candies <= 0:
            print(f'Игра окончена. Игрок {lst[1]} победил')
            break

# candies = 2021
# lst = lottery()
# print(f'Игра начинается. Количество конфет {candies}')
# game_PvP(candies, lst)



# Игра PvB

def lottery() -> list:
    n = random.randint(1, 2)
    lst = []
    if n == 1:
        lst = [1, 'Бот']
    else:
        lst = ['Бот', 1]
    return lst

def game_PvB(candies: int, lst: list):
    if lst[0] == 1:
        while candies > 0:
            n = int(input('Игрок, ваш ход. Напишите сколько конфет вы возьмете (от 1 до 28): '))
            candies -= n
            if candies > 0:
                print(f'Остаток конфет {candies}')
            if candies <= 0:
                print('Игра окончена. Игрок победил')
            print('Бот ходит')
            n = random.randint(1, 28)
            print(f'Бот берет количество конфет = {n}')
            candies -= n
            if candies > 0:
                print(f'Остаток конфет {candies}')
            if candies <= 0:
                print('Игра окончена. Бот победил')
    else:
        while candies > 0:
            print('Бот ходит')
            n = random.randint(1, 28)
            print(f'Бот берет количество конфет = {n}')
            candies -= n
            if candies > 0:
                print(f'Остаток конфет {candies}')
            if candies <= 0:
                print('Игра окончена. Бот победил')
            n = int(input('Игрок, ваш ход. Напишите сколько конфет вы возьмете (от 1 до 28): '))
            candies -= n
            if candies > 0:
                print(f'Остаток конфет {candies}')
            if candies <= 0:
                print('Игра окончена. Игрок победил')

# candies = 2021
# lst = lottery()
# print(f'Игра начинается. Количество конфет {candies}')
# game_PvB(candies, lst)



# Игра PvSmart_Bot

def lottery() -> list:
    n = random.randint(1, 2)
    lst = []
    if n == 1:
        lst = [1, 'Бот']
    else:
        lst = ['Бот', 1]
    return lst

def first_step_smart_Bot(candies: int, max_step: int) -> int:
    n = candies % (max_step + 1)
    print('Бот ходит')
    print(f'Бот берет количество конфет = {n}')
    candies -= n
    if candies > 0:
        print(f'Остаток конфет {candies}')
    if candies <= 0:
        print('Игра окончена. Бот победил')
    return candies
    
def game_PvSmartBot(candies: int, max_step: int):
    while candies > 0:
        n = int(input('Игрок ваш ход. Напишите сколько конфет вы возьмете (от 1 до 28): '))
        candies -= n
        if candies > 0:
            print(f'Остаток конфет {candies}')
        if candies <= 0:
            print('Игра окончена. Игрок 1 победил')
        print('Бот ходит')
        if candies <= 28:
            n = 28
        else:    
            n = (max_step + 1) - n
        print(f'Бот берет количество конфет = {n}')
        candies -= n
        if candies > 0:
            print(f'Остаток конфет {candies}')
        if candies <= 0:
            print('Игра окончена. Бот победил')


candies = 2021
max_step = 28
lst = lottery()
print(f'Игра начинается. Количество конфет {candies}')
if lst[0] == 1:
    print('Или ты знаешь, как победить в этой игре или у меня все-таки есть шанс, посмотрим')
    game_PvSmartBot(candies, max_step)
    # здесь можно допилить еще если человек ошибется, тогда бот тоже точно победит (но не успеваю, к сожалению)
else:
    print('У тебя нет шансов, человек')
    first_step_smart_Bot(candies, max_step)
    game_PvSmartBot(candies, max_step)

