# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

import random

# Игра PvP

def lottery():
    n = random.randint(1, 2)
    lst = []
    if n == 1:
        lst = [1, 2]
    else:
        lst = [2, 1]
    return lst

def game_PvP(candies, lst):
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

# candies = int(121)
# lst = lottery()
# print(f'Игра начинается. Количество конфет {candies}')
# game_PvP(candies, lst)

# Игра PvB

def lottery():
    n = random.randint(1, 2)
    lst = []
    if n == 1:
        lst = [1, 'Бот']
    else:
        lst = ['Бот', 1]
    return lst

def game_PvB(candies, lst):
    
    while candies > 0:
        n = int(input('Игрок {} ваш ход. Напишите сколько конфет вы возьмете (от 1 до 28): '))
        candies -= n
        if candies > 0:
            print(f'Остаток конфет {candies}')
        if candies <= 0:
            print('Игра окончена. Игрок 1 победил')
            break
        print('Бот ходит')
        n = random.randint(1, 28)
        candies -= n
        if candies > 0:
            print(f'Остаток конфет {candies}')
        if candies <= 0:
            print('Игра окончена. Бот победил')
            break

# candies = int(2021)
# print(f'Игра начинается. Количество конфет {candies}')
# game_PvB(candies)

def first_step_smart_Bot(candies, max_step):
    n = candies % (max_step + 1)
    print('Бот ходит')
    print(f'Бот взял {n} конфет')
    candies -= n
    if candies > 0:
        print(f'Остаток конфет {candies}')
    if candies <= 0:
        print('Игра окончена. Бот победил')
    return candies
    
def game_PvSmartBot(candies, max_step):
    
    while candies > 0:
        n = int(input('Игрок ваш ход. Напишите сколько конфет вы возьмете (от 1 до 28): '))
        candies -= n
        if candies > 0:
            print(f'Остаток конфет {candies}')
        if candies <= 0:
            print('Игра окончена. Игрок 1 победил')
            break
        print('Бот ходит')
        if candies <= 28:
            n = 28
        else:    
            n = (max_step + 1) - n
        print(f'Бот взял {n} конфет')
        candies -= n
        if candies > 0:
            print(f'Остаток конфет {candies}')
        if candies <= 0:
            print('Игра окончена. Непобедимый Бот победил')
            break


# candies = int(121)
# max_step = int(28)
# print(f'Игра начинается. Количество конфет {candies}')
# game_PvSmartBot(first_step_smart_Bot(candies, max_step), max_step)

