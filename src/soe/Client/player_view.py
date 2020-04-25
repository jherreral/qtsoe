from PySide2.QtWidgets import (
    QWidget,
    QInputDialog
)

from PySide2.QtCore import Slot

from hand import Hand
from log import Log
from map import Map
from track import Track


class PlayerView(QWidget):
    """
    Holds all the widgets for a player client:
    Hand,Track,Log and Map.
    """

    # def event(self,someEvent):
    #     if someEvent.Type >= QEvent.User:
    #         print("Event was received")
    #     else:
    #         super(PlayerView,self).event(someEvent)

    def __init__(self, parent=None):
        super(PlayerView, self).__init__(parent)

        # Player data

        self.setMinimumSize(800, 600)
        self.log = Log(self)
        self.log.widget.move(600, 100)
        self.track = Track(self)
        self.track.move(600, 300)
        self.hand = Hand(self)
        self.hand.move(0, 400)
        self.map = Map(self)
        self.multiChoice(('asdf', 'qwer'))

    @Slot(tuple)
    def multiChoice(self, choices):
        '''Create a dialog with the choices and show it to the player'''
        choicesAsList = [x for x in choices]
        text, ok = QInputDialog.getItem(self, self.tr("QInputDialog().getText()"), self.tr("User name:"), choicesAsList)
        if text and ok:
            print(text)
        
