import .Client
import .Server

from PySide2.QtWidgets import (
    QApplication,
    QMainWindow
)


def _main():
    app = QApplication([])

    window = QMainWindow()
    window.setMinimumSize(800, 600)

    player_one_view = Client.PlayerView(window)
    game_session = Server.GameSession()
    # zone1.clicked.connect(log.addEntry)
    # QObject.connect(zone1,SIGNAL('clicked()'),log.addEntry)

    # window.setCentralWidget(log)

    # mylabel.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
    window.show()
    # mylabel.adjustSize()
    app.exec_()
    print(str(window.size()))

if __name__ == "__main__":
    main()
