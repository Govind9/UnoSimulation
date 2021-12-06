import random


class Card:
    """A class for a single Card in UNO"""

    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __str__(self):
        ret = ''
        if value is not None:
            ret += value
        if color is not None:
            ret += f' {color}'


class Deck:
    """A class for a group of Cards"""

    def __init__(self, cards):
        self.cards = cards

    def __add__(self, other):
        if isinstance(other, Card):
            cards = self.cards + [other]
        elif isintance(other, Deck):
            cards = self.cards + other.cards
        return Deck(cards)

    def __sub__(self, other):
        if isintance(other, Card):
            


def shuffle(deck):
    cards = deck.cards[::]
    return Deck(random.shuffle(cards))

