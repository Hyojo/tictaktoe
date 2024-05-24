import random


def games():
    element = [" " for _ in range(9)]
    player = input("Выберите x или o: ").lower()

    if player not in ['x', 'o']:
        print("Неверный выбор. Попробуйте снова.")
        return games()

    bot = 'o' if player == 'x' else 'x'
    print_maps(element)
    first_move = random.randint(0, 9)
    while True:
        if first_move > 4:
            if player_move(player, element):
                break
            if bot_move(bot, player, element):
                break
        elif first_move < 5:
            if bot_move(bot, player, element):
                break
            if player_move(player, element):
                break
    new_game = input("Если хотите сыграть снова введите '1': ")
    try:
        if int(new_game) == 1:
            return games()
    except ValueError:
        exit(0)


def player_move(player, element):
    if " " not in element:
        print("Ничья")
        return True

    ch = int(input("Выберите ячейку (0-8): "))
    if 0 <= ch <= 8 and element[ch] == " ":
        element[ch] = player
    else:
        print("Неверный ход, попробуйте снова.")
        return player_move(player, element)

    print_maps(element)
    return check_end_game(element)


def brain_bot(bot, player, element):
    for i in range(len(element)):
        if element[i] == " ":
            element[i] = bot
            if check_winning(bot, element):
                return i
            element[i] = " "
    rand = random.randint(0, 9)
    if rand > 2:
        for i in range(len(element)):
            if element[i] == " ":
                element[i] = player
                if check_winning(player, element):
                    return i
                element[i] = " "

    # if element[int(len(element) / 2)] == " ":
    #     return int(len(element) / 2)

    rand = random.randint(0, 9)
    if rand > 6 and " " in element:
        relement = []
        for i in [0, 2, 6, 8]:
            if element[i] == ' ':
                relement.append(i)
        if relement:
            i = random.randint(0, len(relement) - 1)
            return relement[i]
    else:
        for i in range(9):
            if element[i] == ' ':
                return i


def bot_move(bot, player, element):
    if " " not in element:
        print("Ничья")
        return True

    # ch = random.randint(0, 8)
    # while element[ch] != " ":
    #     ch = random.randint(0, 8)
    #
    # element[ch] = bot

    ch = brain_bot(bot, player, element)
    element[ch] = bot
    print_maps(element)
    return check_end_game(element)


def print_maps(element):
    maps = f"""
     {element[0]} | {element[1]} | {element[2]}              0 | 1 | 2
    ---+---+---            ---+---+---
     {element[3]} | {element[4]} | {element[5]}              3 | 4 | 5
    ---+---+---            ---+---+---
     {element[6]} | {element[7]} | {element[8]}              6 | 7 | 8
    """
    print(maps)


def check_end_game(element):
    winn_comb = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
        (0, 4, 8), (2, 4, 6)  # diagonal
    ]

    for (a, b, c) in winn_comb:
        if element[a] == element[b] == element[c] and element[a] != " ":
            print(f'Выиграли {element[a]}')
            return True
    return False


def check_winning(player, element):
    winn_comb = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
        (0, 4, 8), (2, 4, 6)  # diagonal
    ]

    for i in winn_comb:
        if element[i[0]] == element[i[1]] == element[i[2]] == player:
            return True
    return False


games()
