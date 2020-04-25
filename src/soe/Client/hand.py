from PySide2.QtWidgets import (
    QWidget,
    QGridLayout,
    QLabel,
    QPushButton
)
from PySide2.QtCore import Qt


class Hand(QWidget):
    def __init__(self, parent=None, width=300, height=150):
        super(Hand, self).__init__(parent)
        self.mainLayout = QGridLayout()
        self.setLayout(self.mainLayout)
        self.setMinimumSize(width, height)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.red)
        self.setPalette(p)

        self.factionName = "Communist"
        self.playerName = "Karen"
        factionNameLabel = QLabel(self.factionName)
        factionIconLabel = QLabel("Placeholder")
        playerNameLabel = QLabel(self.playerName)

        self.mainLayout.addWidget(playerNameLabel, 2, 1)
        self.mainLayout.addWidget(factionIconLabel, 1, 2)
        self.mainLayout.addWidget(factionNameLabel, 2, 2)

        # Create cards
        self.CreatePlaceholderCards()

    def CreatePlaceholderCards(self):
        self.cardsLayout = QGridLayout()
        self.cardsLayout.addWidget(QPushButton("Placeholder 1"), 1, 1)
        self.cardsLayout.addWidget(QPushButton("Placeholder 2"), 1, 2)
        self.cardsLayout.addWidget(QPushButton("Placeholder 3"), 1, 3)
        self.mainLayout.addLayout(self.cardsLayout, 1, 1)
