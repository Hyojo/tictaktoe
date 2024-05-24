class Card:
    def __init__(self, suit, value, symbol):
        self.suit = suit
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return f'{self.suit} {self.value} {self.symbol}'


def gamestart():
    deck = init_deck()



def init_deck():
    suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    cards = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5,
             '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
             'J': 10, 'Q': 10, 'K': 10}
    suit_symbols = {'Hearts': '\u2661', 'Diamonds': '\u2662',
                    'Spades': '\u2664', 'Clubs': '\u2667'}
    deck = []
    for suit in suits:
        for card, value in cards.items():
            deck.append(Card(card, value, suit_symbols[suit]))
    return deck


if __name__ == '__main__':
    gamestart()
