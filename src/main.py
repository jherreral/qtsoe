from PySide2.QtWidgets import (QApplication,
QMainWindow,QLabel,QPlainTextEdit,QPushButton,
QSizePolicy,QVBoxLayout,QGridLayout,QWidget,QInputDialog)
from PySide2.QtGui import QPixmap,QImage
from PySide2.QtCore import Qt,SIGNAL


class QLabelButton(QLabel):

    def __init(self, parent):
        QLabel.__init__(self, parent)

    def enterEvent(self, ev):
        self.emit(SIGNAL('hoverIn()'))

    def leaveEvent(self, ev):
        self.emit(SIGNAL('hoverOut()'))

    def mousePressEvent(self, ev):
        self.emit(SIGNAL('clicked()'))

class Zone(QWidget):
    def __init__(self, parent=None, *args):
        super(Zone, self).__init__(parent)
        self.setMinimumSize(300, 350)
        self.setMaximumSize(300, 350)

        self.pinkPixmap = QPixmap('C:/Users/jherr/qtsoe/assets/japan.png')
        self.whitePixmap = self.pinkPixmap.copy()
        self.whitePixmap.fill()

        self.button = QLabelButton(self)
        self.button.setPixmap(self.pinkPixmap)
        self.button.setScaledContents(True)
        self.button.setMask(self.pinkPixmap.mask()) # THIS DOES THE MAGIC

        self.connect(self.button, SIGNAL('clicked()'), self.onClick)
        self.connect(self.button, SIGNAL('hoverIn()'), self.onEnter)
        self.connect(self.button, SIGNAL('hoverOut()'), self.onLeave)

    def onClick(self):
        print('Button was clicked')

    def onEnter(self):
        print('Inside')
        self.button.setPixmap(self.whitePixmap)

    def onLeave(self):
        print('Outside')
        self.button.setPixmap(self.pinkPixmap)



class Map(QWidget):
    def __init__(self,parent=None,width=400,height=400):
        super(Map,self).__init__(parent)


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
        



class Log(QPlainTextEdit):
    def __init__(self,parent=None,width=150,height=150):
        super(Log,self).__init__(parent)
        self.setPlainText("ASDFASDFVXCVXC VsdfsdfadVBXBXCBV XDfsdfsdf")
        self.resize(width,height)
        self.setReadOnly(True)
        self.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)

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


app = QApplication([])

window = QMainWindow()
window.setMinimumSize(800,600)
log = Log(window)
log.move(600,100)
track = Track(window)
track.move(600,300)
hand=Hand(window)
hand.move(0,400)
zone1=Zone(window)

#window.setCentralWidget(log)

#mylabel.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
print(str(window.size()))
print(str(log.size()))
window.show()
#mylabel.adjustSize()
print(str(window.size()))
print(str(log.size()))
app.exec_()
print(str(window.size()))
print(str(log.size()))
