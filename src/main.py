from PySide2.QtWidgets import (
    QApplication,
    QMainWindow
)

from player_view import PlayerView

app = QApplication([])

window = QMainWindow()
window.setMinimumSize(800, 600)

playerOneView = PlayerView(window)

# zone1.clicked.connect(log.addEntry)
# QObject.connect(zone1,SIGNAL('clicked()'),log.addEntry)

# window.setCentralWidget(log)

# mylabel.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
window.show()
# mylabel.adjustSize()
app.exec_()
print(str(window.size()))
