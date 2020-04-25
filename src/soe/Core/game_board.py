"""Game Board."""

class Card:
    def __init__(self):
        self._name = None
        self._id = None

class GameBoard:
    def __init__(self):
        self._map = None
        self._discard_deck = None
        self._special_deck = None
        self._turn_deck = None
