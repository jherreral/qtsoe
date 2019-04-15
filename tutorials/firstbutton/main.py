import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import Slot

# Greetings
@Slot()
def say_hello():
    print("Button clicked,hello!")

#Create the QtApplication
app = QApplication(sys.argv)

#Create button
button = QPushButton("Click me")

#Connect the button to the function
button.clicked.connect(say_hello)

#Show b utton
button.show()

#Run the main Qt loop
app.exec_()