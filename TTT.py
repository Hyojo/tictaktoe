import random


def games():
    element = [" " for _ in range(9)]
    player = input("Выберите x или o: ").lower()

    if player not in ['x', 'o']:
        print("Неверный выбор. Попробуйте снова.")
        return games()

    bot = 'o' if player == 'x' else 'x'
    print_maps(element)

    while " " in element:
        player_choose(element, player, True)
        print_maps(element)
        if not end_game(element):
            return
        if " " in element:
            player_choose(element, bot, False)
            print_maps(element)
            if not end_game(element):
                return
        else:
            print("Ничья")
            break


def player_choose(element, player, is_human):
    if is_human:
        try:
            ch = int(input("Выберите ячейку: "))
            if ch not in range(9):
                raise ValueError
        except ValueError:
            print("Неверный выбор. Попробуйте снова.")
            return player_choose(element, player, is_human)
    else:
        ch = random.randint(0, 8)

    if element[ch] == " ":
        element[ch] = player
    else:
        if is_human:
            print("Ячейка занята. Попробуйте снова.")
        player_choose(element, player, is_human)


def print_maps(element):
    maps = f"""
     {element[0]} | {element[1]} | {element[2]}
    ---+---+---
     {element[3]} | {element[4]} | {element[5]}
    ---+---+---
     {element[6]} | {element[7]} | {element[8]}
    """
    print(maps)


def end_game(element):
    winn_comb = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
        (0, 4, 8), (2, 4, 6)  # diagonal
    ]

    for (a, b, c) in winn_comb:
        if element[a] == element[b] == element[c] and element[a] != " ":
            print(f'Выиграли {element[a]}')
            return False
    return True


games()
