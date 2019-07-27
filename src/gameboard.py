from enum import Enum


class Phase(Enum):
    MOBILIZ = 0
    TURN = 1


class GameState:
    def __init__(self):
        self.playerOrder = []
        self.phase = Phase.MOBILIZ


class Zone:
    def __init__(self):
        self.name = None
        self.sphere = None
        self.production = None
        self.oil = None
        self.compass = None
        self.capital = None


class GameBoard:
    def __init__(self, players):
        self.mapGraph = None
        self.specialDeck = None
        self.discardDeck = None
        self.zones = {}
        self.round = None
        self.gameState = None
        self.players = None

    def loadFromAssets(self):
        """
        Load data from assets in disc to RAM,
        creating all the necessary game objects
        """
        self.parseZones()
        self.parseEdges()

    def parseZones(self):
        with open("../assets/zonesData.csv", 'r') as f:
            for line in f.readlines():
                data = line.split(';')
                keyName = data[0]
                zone = Zone()
                zone.id = int(data[1])
                zone.sphere = int(data[2])
                zone.production = int(data[3])
                zone.oil = int(data[4])
                zone.compass = bool(int(data[5]))
                zone.capital = bool(int(data[6]))
                self.zones[keyName] = zone
            f.close()

    def parseEdges(self):
        with open('../assets/IncidenceT2.txt', 'r') as f:
            for line in f.readlines():
                nodeA = int(line.find('1'))
                nodeB = int(line.find('1', nodeA+1))
                self.mapGraph.append(nodeA, nodeB)
            f.close()


class Player:
    def __init(self):
        self.user = None
        self.name = None
        self.faction = None
        self.hand = None
        self.team = None
        self.capital = None
