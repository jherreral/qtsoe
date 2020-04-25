"""Map data structure."""


class Zone:
    def __init__(self):
        self._oil = None
        self._production = None
        self._capital = None
        self._sphere = None
        self._name = None
        self._id = None
        self._units = None
        self._faction = None
        self._sea = None
        self._capital = None
        self._interest = None

class Graph:
    def __init__(self):
        self._graph_data = None

    def get_connections(self,zone:Zone):
        pass

class GameMap:
    def __init__(self):
        self._zones = None
        self._graph = None

    def list_zones(self,player:Player):
        pass

    def get_player_oil(self,player:Player):
        pass

    def get_player_production(self,player:Player):
        pass

    def get_player_spheres(self,player:Player):
        pass

    def get_player_capitals(self,player:Player):
        pass


    