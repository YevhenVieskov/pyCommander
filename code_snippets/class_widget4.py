# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 19:11:08 2023

@author: Yevhen_Vieskov
"""

from PySide2.QtWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.central = QWidget()
        self.central.setObjectName("Central_Widget")
        self.setCentralWidget(self.central)
        mainLayout = QHBoxLayout(self.central)
        self.central.setStyleSheet("""
        #Central_Widget{
            background-color: #2489FF;
        }""")

        #init mainView widget
        self.leftSide = leftWindow(self.central)
        self.rightSide = rightWindow(self.central)

        mainLayout.addWidget(self.leftSide)
        mainLayout.addWidget(self.rightSide)

class leftWindow(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setObjectName("leftWindow")
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.label = QLabel(" Left ")
        self.leftButton = customBtn(" Left Button ", "someSVGHere", self)
        layout.addWidget(self.label)
        layout.addWidget(self.leftButton)

        self.setStyleSheet("border : 2px solid white;")


class rightWindow(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setObjectName("rightWindow")
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.label = QLabel(" Right ")
        self.rightButton = customBtn(" Right Button ", "someSVGHere", self)
        layout.addWidget(self.label)
        layout.addWidget(self.rightButton)

        self.setStyleSheet("border : 2px solid black;")


class customBtn(QWidget):
    def __init__(self, text, svgIcon, parent):
        super().__init__(parent)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.btnText = QLabel(text)
        self.Icon = svgIcon
        layout.addWidget(self.btnText)
        # setup the icon and the stylesheet etc ....

    def mouseReleaseEvent(self, event):
        # if it's the right button getting clicked, change the stylesheet of the central widget in main window
        # How do I do that here ???
        return super().mouseReleaseEvent(event)
        

# Launcher
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.setWindowTitle("nesting test")
    win.show()
    sys.exit(app.exec_())
    
    
'''


Generally speaking, when dealing with object hierarchy, child objects should not attempt to directly interact their parents. In fact, they should always be able to "work" on their own, no matter of their parent, and even when they have no parent at all.

Considering this, instead of connecting a signal to a slot of a [great-][grand]parent, it should be that parent that connects the [great-][grand]child signal to its own slot. This perspective is important, because it's also what allows us to connect sibling objects that are (nor could) be aware of each other.

class customBtn(QWidget):
    customSignal = pyqtSignal(Qt.MouseButton)

    def mouseReleaseEvent(self, event):
        self.customSignal.emit(event.button())


class MainWindow(QMainWindow):
    def __init__(self):
        # ...
        self.leftSide = leftWindow(self.central)
        self.leftSide.leftButton.customSignal.connect(self.something)

    def something(self):
        # whatever

If the structure has many levels, it's also good practice to create custom signals for the intermediate classes, since signals can also be chained as long as they have a compatible signature (the target signal must have the same argument types or fewer arguments with same types).

class leftWindow(QWidget):
    customSignal = pyqtSignal()
    def __init__(self, parent):
        # ...
        self.leftButton = customBtn(" Left Button ", "someSVGHere", self)
        self.leftButton.customSignal.connect(self.customSignal)

class MainWindow(QMainWindow):
    def __init__(self):
        # ...
        self.leftSide = leftWindow(self.central)
        self.leftSide.customSignal.connect(self.something)

In the case above, the signal of leftWindow doesn't have any arguments, so it's compatible with the button signal, as those arguments will be automatically discarded.
'''    
    