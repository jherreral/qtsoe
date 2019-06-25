from PySide2.QtWidgets import (QApplication,
QMainWindow,QLabel,QPlainTextEdit,QPushButton,
QSizePolicy,QVBoxLayout,QGridLayout,QWidget,QInputDialog)
from PySide2.QtGui import QPixmap,QImage
from PySide2.QtCore import Qt,SIGNAL,QObject,Signal,Slot,QEvent,QCoreApplication

import gameboard as gb
from os import getcwd
import logging

class Zone(QPushButton):
    """
    Visible object that represents a zone in the game board. It allows the user
    to respond to requests made by the Game Master.
    pinkPixmap is the non-visible, interactive part of the widget (the button).
    whitePixmap is the visible, non-interactive part (the canvas).
    """
    zoneActivated = Signal(str)

    def __init__(self, parent=None, name = "Empty", position = (0,0), size = (10,10),scale=1.0,*args):
        super(Zone, self).__init__(parent)

        self.name = name
        self.selectable = False
        self.selected = False

        scaledX=position[0]*scale
        scaledY=position[1]*scale
        scaledW=size[0]*scale
        scaledH=size[1]*scale
        self.move(scaledX,scaledY)
        self.setMinimumSize(scaledW, scaledH)
        #self.setMaximumSize(300, 350)
        self.pinkPixmap = QPixmap('assets/zonesBitmaps/'+name+'.png')
        self.pinkPixmap = self.pinkPixmap.scaledToWidth(scaledW)
        self.whitePixmap = self.pinkPixmap.copy()
        self.whitePixmap.fill()

        self.label = QLabel(self)
        self.label.setPixmap(self.pinkPixmap)
        self.label.setScaledContents(True)

        
        self.setMask(self.pinkPixmap.mask()) # THIS DOES THE MAGIC

        #self.connect(self.button, SIGNAL('clicked()'), self.onClick)
        #self.button.clicked.connect(self.onClick())
        #self.connect(self.button, SIGNAL('hoverIn()'), self.onEnter)
        #self.connect(self.button, SIGNAL('hoverOut()'), self.onLeave)

    def enterEvent(self, ev):
        #self.emit(SIGNAL('hoverIn()'))
        self.label.setPixmap(self.whitePixmap)
        #print('Inside')

    def leaveEvent(self, ev):
        #self.emit(SIGNAL('hoverOut()'))
        self.label.setPixmap(self.pinkPixmap)
        #print('Outside')

    def mousePressEvent(self, ev): 
        self.zoneActivated.emit(self.name+' was clicked')
        print(self.name + ' clicked')

class Hand(QWidget):
    def __init__(self,parent=None,width=300,height=150):
        super(Hand,self).__init__(parent)
        self.mainLayout = QGridLayout()
        self.setLayout(self.mainLayout)
        self.setMinimumSize(width,height)
        
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(),Qt.red)
        self.setPalette(p)

        self.factionName = "Communist"
        self.playerName = "Karen"
        factionNameLabel = QLabel(self.factionName)
        factionIconLabel = QLabel("Placeholder")
        playerNameLabel = QLabel(self.playerName)

        self.mainLayout.addWidget(playerNameLabel,2,1)
        self.mainLayout.addWidget(factionIconLabel,1,2)
        self.mainLayout.addWidget(factionNameLabel,2,2)

        #Create cards
        self.CreatePlaceholderCards()


    def CreatePlaceholderCards(self):
        self.cardsLayout = QGridLayout()
        self.cardsLayout.addWidget(QPushButton("Placeholder 1"),1,1)
        self.cardsLayout.addWidget(QPushButton("Placeholder 2"),1,2)
        self.cardsLayout.addWidget(QPushButton("Placeholder 3"),1,3)
        self.mainLayout.addLayout(self.cardsLayout,1,1)

class Log(logging.Handler):
    def __init__(self,parent=None,width=150,height=150):
        super().__init__()
        self.widget = QPlainTextEdit(parent)
        self.widget.setPlainText("Placeholder log text\n")
        self.widget.resize(width,height)
        self.widget.setReadOnly(True)
        self.widget.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)

    @Slot()
    @Slot(str)
    def addEntry(self,text='blo'):
        self.widget.appendPlainText(text)
        print('appending')

class Track(QWidget):
    def __init__(self,parent=None,width=150,height=150):
        super(Track,self).__init__(parent)
        self.mainLayout = QGridLayout()
        self.setLayout(self.mainLayout)
        self.setMinimumSize(width,height)

        # Paint background
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(),Qt.blue)
        self.setPalette(p)

        firstCol = QGridLayout()
        firstCol.addWidget(QLabel("Prod"),1,1)
        firstCol.addWidget(QLabel("Oil"),2,1)
        firstCol.addWidget(QLabel("Sph"),3,1)
        firstCol.addWidget(QLabel("Caps"),4,1)
        self.mainLayout.addLayout(firstCol,1,1)
        t_data = [[10,20,30,40],[11,22,33,44],[12,22,32,42],[13,23,33,43]]
        self.CreatePlayerColumns(t_data)

    def CreatePlayerColumns(self,data):
        playerColumns = QGridLayout()
        for idx,p in enumerate(data):
            col = idx +1
            playerColumns.addWidget(QLabel(str(p[0])),1,col)
            playerColumns.addWidget(QLabel(str(p[1])),2,col)
            playerColumns.addWidget(QLabel(str(p[2])),3,col)
            playerColumns.addWidget(QLabel(str(p[3])),4,col)
        self.mainLayout.addLayout(playerColumns,1,2)

class Map(QWidget):
    """
    Holds all interactive zones
    """

    def __init__(self,parent=None,width=400,height=450):
        super(Map,self).__init__(parent)
        self.scale = width / 826.0
        self.zones = {}
        self.parent=parent
        self.loadFromAssets()

    def loadFromAssets(self):
        self.createBackground()
        self.createZones()

    def createZones(self):
        """
        100mm are equal to 378 px.
        'Real' width is 680 px
        """
        with open('assets/mapCoords.csv','r') as f:
            f.readline()
            for line in f:
                (name,x,y,w,h) = line.split(",")
                x=int(x)
                y=int(y)
                w=int(w)
                h=int(h)
                zone = Zone(self,name,(x,y),(w,h),self.scale)
                zone.zoneActivated.connect(self.parent.log.addEntry)
                self.zones[name] = zone

    def createBackground(self):
        pass
    
    def setPossibleZones(self,zoneList):
        for zoneName in zoneList:
            self.zones[zoneName].selectable = True


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

    def __init__(self,parent=None):
        super(PlayerView,self).__init__(parent)

        # Player data

        self.setMinimumSize(800,600)
        self.log = Log(self)
        self.log.widget.move(600,100)
        self.track = Track(self)
        self.track.move(600,300)
        self.hand=Hand(self)
        self.hand.move(0,400)
        self.map = Map(self)

        #self.zone1=Zone(self)
        
        #Zone.zoneActivated.connect(self.log.addEntry)

app = QApplication([])

window = QMainWindow()
window.setMinimumSize(800,600)

playerOneView = PlayerView(window)

#zone1.clicked.connect(log.addEntry)
#QObject.connect(zone1,SIGNAL('clicked()'),log.addEntry)

#window.setCentralWidget(log)

#mylabel.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
window.show()
#mylabel.adjustSize()
app.exec_()
print(str(window.size()))
