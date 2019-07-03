from logging import Handler
from PySide2.QtWidgets import (
    QPlainTextEdit
)
from PySide2.QtCore import Slot


class Log(Handler):
    def __init__(self, parent=None, width=150, height=150):
        super().__init__()
        self.widget = QPlainTextEdit(parent)
        self.widget.setPlainText("Placeholder log text\n")
        self.widget.resize(width, height)
        self.widget.setReadOnly(True)
        self.widget.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)

    @Slot()
    @Slot(str)
    def addEntry(self, text='blo'):
        self.widget.appendPlainText(text)
        print('appending')
