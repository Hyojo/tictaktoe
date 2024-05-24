import random

element = [" ", " ", " ", " ", " ", " ", " ", " ", " ", ]


def games():
    global element
    player = input("Выберите x или o: ")
    bot = ""
    if player == 'x':
        bot = 'o'
    elif player == 'o':
        bot = 'x'
    else:
        games()
    print_maps()
    while True:
        if " " in element:
            player_choose(player, True)
            print_maps()
            if not end_game(element):
                break
        else:
            print("Ничья")
            break
        if " " in element:
            player_choose(bot, False)
            print_maps()
            if not end_game(element):
                break
        else:
            print("Ничья")
            break


def player_choose(player, check):
    ch = ''
    if check:
        ch = int(input("Выберите ячейку: "))
    else:
        ch = random.randint(0, 8)
    if element[ch] == " ":
        element[ch] = player
    else:
        player_choose(player, check)


def print_maps():
    maps = f"""
     {element[0]} | {element[1]} | {element[2]}
    ---+---+---
     {element[3]} | {element[4]} | {element[5]}
    ---+---+---
     {element[6]} | {element[7]} | {element[8]}
    """
    print(maps)


def end_game(elements):
    for i in range(0, 7, 3):
        if (element[i] == element[i + 1] == element[i + 2]) and elements[i] != " ":
            print(f'Выиграли {element[i]}')
            return False
    for i in range(0, 3):
        if (element[i] == element[i + 3] == element[i + 6]) and elements[i] != " ":
            print(f'Выиграли {element[i]}')
            return False
    if (element[0] == element[4] == element[8]) and elements[4] != " ":
        print(f'Выиграли {element[4]}')
        return False
    elif (element[2] == element[4] == element[6]) and elements[4] != " ":
        print(f'Выиграли {element[4]}')
        return False
    else:
        return True


games()
