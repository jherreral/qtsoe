from PySide2.QtWidgets import (
    QPushButton,
    QLabel
)
from PySide2.QtGui import (
    QPixmap,
    QColor
)
from PySide2.QtCore import (
    Signal
)


class Zone(QPushButton):
    """
    Visible object that represents a zone in the game board. It allows the user
    to respond to requests made by the Game Master.
    pinkPixmap is the non-visible, interactive part of the widget (the button).
    whitePixmap is the visible, non-interactive part (the canvas).
    """
    zoneActivated = Signal(str)
    zoneSelected = Signal(str)

    @property
    def selectable(self):
        return self._selectable

    @selectable.setter
    def selectable(self, value):
        self._selectable = value
        if self._selectable:
            self.label.setPixmap(self.pinkPixmap)
        else:
            self.label.setPixmap(self.greyPixmap)

    def __init__(self, parent=None, name="Empty", position=(0, 0),
                 size=(10, 10), scale=1.0, *args):
        super(Zone, self).__init__(parent)

        self.name = name
        self._selectable = False
        self.hold = False
        self.selected = False

        scaledX = position[0]*scale
        scaledY = position[1]*scale
        scaledW = size[0]*scale
        scaledH = size[1]*scale
        self.move(scaledX, scaledY)
        self.setMinimumSize(scaledW, scaledH)
        # self.setMaximumSize(300, 350)
        self.pinkPixmap = QPixmap('assets/zonesBitmaps/'+name+'.png')
        self.pinkPixmap = self.pinkPixmap.scaledToWidth(scaledW)
        self.whitePixmap = self.pinkPixmap.copy()
        self.whitePixmap.fill()
        self.greyPixmap = self.pinkPixmap.copy()
        self.greyPixmap.fill(QColor(100, 100, 100))
        # Done: Turn 'selectable' into a property that sets the unhover pixmap
        self.label = QLabel(self)
        self.label.setPixmap(self.greyPixmap)
        self.label.setScaledContents(True)

        self.setMask(self.pinkPixmap.mask())  # THIS DOES THE MAGIC

        # self.connect(self.button, SIGNAL('clicked()'), self.onClick)
        # self.button.clicked.connect(self.onClick())
        # self.connect(self.button, SIGNAL('hoverIn()'), self.onEnter)
        # self.connect(self.button, SIGNAL('hoverOut()'), self.onLeave)

    def enterEvent(self, ev):
        # self.emit(SIGNAL('hoverIn()'))
        if self.selectable:
            self.label.setPixmap(self.whitePixmap)
        # print('Inside')

    def leaveEvent(self, ev):
        # self.emit(SIGNAL('hoverOut()'))
        if self.selectable:
            self.label.setPixmap(self.pinkPixmap)

        # print('Outside')

    def mousePressEvent(self, ev):
        if self.selectable:
            if not self.selected:
                self.zoneActivated.emit(self.name+' was clicked')
                print(self.name + ' clicked')
                self.zoneSelected.emit(self.name)
                if self.hold:
                    self.selected = True
            else:
                self.selected = False
