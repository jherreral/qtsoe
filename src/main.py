from PySide2.QtWidgets import (QApplication,
QMainWindow,QLabel,QPlainTextEdit,
QSizePolicy,QVBoxLayout,QGridLayout,QWidget,QInputDialog)

class Hand(Qwidget):
    def __init__(self,parent=None,width=300,height=150):
        super(Hand,self).__init__(parent)
        self.mainLayout = QGridLayout()
        self.setLayout(self.mainLayout)
        self.setMinimumSize(width,height)

        self.factionName = "Communist"
        self.playerName = "Karen"
        factionNameLabel = QLabel(self.factionName)
        factionIconLabel = QLabel("Placeholder")
        playerNameLabel = QLabel(self.factionName)

        self.mainLayout.addWidget(playerNameLabel,2,1)
        self.mainLayout.addWidget(factionIconLabel,1,2)
        self.mainLayout.addWidget(factionNameLabel,2,2)

        #Create cards
        self.CreatePlaceholderCards()


    def CreatePlaceholderCards(self):
        self.cardsLayout = QGridLayout()
        



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
log.move(500,100)
track = Track(window)
lisss=ListChooser(window)

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
