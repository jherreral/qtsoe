from gameboard import GameBoard


class GameMaster:
    """
    Manages the game board and the flow of the game.
    Has the initializeBoard() to setup the board,
    play() to start or resume the game.
    """

    def __init__(self):
        self.gb = GameBoard()

    def play(self):
        pass

    def dealCapitals(self):
        '''Send Request to all players to choose their capital'''
        capitalPairs = self.gb.getCapitalPairs()
        for player in self.gb.players:
            #Trigger somehow a multichoice slot of playerview
            pass
            
            