from PySide2.QtWidgets import (QApplication,
QMainWindow,QLabel,QPlainTextEdit,
QSizePolicy,QVBoxLayout,QGridLayout,QWidget)

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
        firstCol.addWidget(QLabel("A"),1,1)
        firstCol.addWidget(QLabel("A"),2,1)
        firstCol.addWidget(QLabel("A"),3,1)
        firstCol.addWidget(QLabel("A"),4,1)
        self.mainLayout.addLayout(firstCol,1,1)


app = QApplication([])

window = QMainWindow()
window.setMinimumSize(800,600)
log = Log(window)
log.move(500,100)
track = Track(window)

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
