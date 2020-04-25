"""Game session running in the server."""
from enum import IntFlag,auto


class Phase(IntFlag):
    MOBI_START = auto()
    MOBI_ARRANGE_TURN_DECK = auto()
    MOBI_PLACING_UNITS = auto()
    MOBI_END = auto()
    TURN_ACTION = auto()
    TURN_COMBAT_DECLARE_ATTACK = auto()
    TURN_COMBAT_DICE_ROLLED = auto()
    TURN_MOVEMENT = auto()
    TURN_END = auto()

class Player:
    def __init__(self):
        self._name = None
        self._id = None
        self._hand = None
        self._faction = None
        self._team = None

class DeclaredAttack:
    def __init__(self):
        self._attacker = None
        self._defender = None
        self._attacking_zone = None
        self._defending_zone = None

class GameSession:
    def __init__(self):
        self._board = None
        self._players = None
        self._ongoing_effects = None
        self._log = None
        self._round = None
        self._phase = None
        self._turn = None
        self._actions = None
        self._mobi_order = None
        self._current_player = None
        self._declared_attack = None
        self._server_ref = None

