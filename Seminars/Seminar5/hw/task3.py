# Создайте программу для игры в "Крестики-нолики".

# 1 - крестик
# 2 - нолик


def match_with_win_combinations_1(lst: list[int]) -> int:
    if lst[0][0] == 1 and lst[0][1] == 1 and lst[0][2] == 1:
        return 1
    elif lst[1][0] == 1 and lst[1][1] == 1 and lst[1][2] == 1:
        return 1    
    elif lst[2][0] == 1 and lst[2][1] == 1 and lst[2][2] == 1:
        return 1  
    elif lst[0][0] == 1 and lst[1][0] == 1 and lst[2][0] == 1:
        return 1  
    elif lst[0][1] == 1 and lst[1][1] == 1 and lst[2][1] == 1:
        return 1  
    elif lst[0][2] == 1 and lst[1][2] == 1 and lst[2][2] == 1:
        return 1  
    elif lst[0][0] == 1 and lst[1][1] == 1 and lst[2][1] == 1:
        return 1  
    elif lst[0][2] == 1 and lst[1][1] == 1 and lst[2][0] == 1:
        return 1  


def match_with_win_combinations_2(lst: list[int]) -> int:
    if lst[0][0] == 1 and lst[0][1] == 1 and lst[0][2] == 2:
        return 1
    elif lst[1][0] == 1 and lst[1][1] == 1 and lst[1][2] == 2:
        return 1    
    elif lst[2][0] == 1 and lst[2][1] == 1 and lst[2][2] == 2:
        return 1  
    elif lst[0][0] == 1 and lst[1][0] == 1 and lst[2][0] == 2:
        return 1  
    elif lst[0][1] == 1 and lst[1][1] == 1 and lst[2][1] == 2:
        return 1  
    elif lst[0][2] == 1 and lst[1][2] == 1 and lst[2][2] == 2:
        return 1  
    elif lst[0][0] == 1 and lst[1][1] == 1 and lst[2][1] == 2:
        return 1  
    elif lst[0][2] == 1 and lst[1][1] == 1 and lst[2][0] == 2:
        return 1  

def print_matrix(lst: list[int]):
    for i in range(len(lst)):
        print(lst[i])

lst = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print_matrix(lst)
steps = 9
while steps > 5: 
    print('Игрок 1 делает ход')
    lst[int(input('введите строку, на которую хотите поставить элемент (0-1я строка, 1-2я строка, 2-3я строка): '))]\
        [int(input('введите позицию, на которую хотите поставить элемент (0-1ый элемент, 1-2й элемент, 2-3й элемент)'))] = 1
    print_matrix(lst)
    steps -= 1
    print('Игрок 2 делает ход')
    lst[int(input('введите строку, на которую хотите поставить элемент (0-1я строка, 1-2я строка, 2-3я строка): '))]\
        [int(input('введите позицию, на которую хотите поставить элемент (0-1ый элемент, 1-2й элемент, 2-3й элемент)'))] = 2
    print_matrix(lst)
    steps -= 1

while steps > 1:
    print('Игрок 1 делает ход')
    lst[int(input('введите строку, на которую хотите поставить элемент (0-1я строка, 1-2я строка, 2-3я строка): '))]\
        [int(input('введите позицию, на которую хотите поставить элемент (0-1ый элемент, 1-2й элемент, 2-3й элемент)'))] = 1
    print_matrix(lst)
    match_with_win_combinations_1(lst)
    if match_with_win_combinations_1(lst) == 1:
        print('Игра окончена. Игрок 1 победил')
        break
    steps -= 1
    print('Игрок 2 делает ход')
    lst[int(input('введите строку, на которую хотите поставить элемент (0-1я строка, 1-2я строка, 2-3я строка): '))]\
        [int(input('введите позицию, на которую хотите поставить элемент (0-1ый элемент, 1-2й элемент, 2-3й элемент)'))] = 2
    print_matrix(lst)
    match_with_win_combinations_2(lst)
    if match_with_win_combinations_2(lst) == 1:
        break
    steps -= 1
