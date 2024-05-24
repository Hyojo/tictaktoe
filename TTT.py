import random


def games():
    element = [" " for _ in range(9)]
    player = input("Выберите x или o: ").lower()

    if player not in ['x', 'o']:
        print("Неверный выбор. Попробуйте снова.")
        return games()

    bot = 'o' if player == 'x' else 'x'
    print_maps(element)
    while True:
        if player_move(player, element):
            break
        if bot_move(bot, element):
            break


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


def bot_move(bot, element):
    if " " not in element:
        print("Ничья")
        return True

    ch = random.randint(0, 8)
    while element[ch] != " ":
        ch = random.randint(0, 8)

    element[ch] = bot
    print_maps(element)
    return check_end_game(element)


def print_maps(element):
    maps = f"""
     {element[0]} | {element[1]} | {element[2]}
    ---+---+---
     {element[3]} | {element[4]} | {element[5]}
    ---+---+---
     {element[6]} | {element[7]} | {element[8]}
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


games()
