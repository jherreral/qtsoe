from PySide2.QtWidgets import (
    QWidget,
    QGridLayout,
    QLabel
)
from PySide2.QtCore import Qt


class Track(QWidget):
    def __init__(self, parent=None, width=150, height=150):
        super(Track, self).__init__(parent)
        self.mainLayout = QGridLayout()
        self.setLayout(self.mainLayout)
        self.setMinimumSize(width, height)

        # Paint background
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.blue)
        self.setPalette(p)

        firstCol = QGridLayout()
        firstCol.addWidget(QLabel("Prod"), 1, 1)
        firstCol.addWidget(QLabel("Oil"), 2, 1)
        firstCol.addWidget(QLabel("Sph"), 3, 1)
        firstCol.addWidget(QLabel("Caps"), 4, 1)
        self.mainLayout.addLayout(firstCol, 1, 1)
        t_data = [[10, 20, 30, 40], [11, 22, 33, 44],
                  [12, 22, 32, 42], [13, 23, 33, 43]]
        self.CreatePlayerColumns(t_data)

    def CreatePlayerColumns(self, data):
        playerColumns = QGridLayout()
        for idx, p in enumerate(data):
            col = idx + 1
            playerColumns.addWidget(QLabel(str(p[0])), 1, col)
            playerColumns.addWidget(QLabel(str(p[1])), 2, col)
            playerColumns.addWidget(QLabel(str(p[2])), 3, col)
            playerColumns.addWidget(QLabel(str(p[3])), 4, col)
        self.mainLayout.addLayout(playerColumns, 1, 2)
