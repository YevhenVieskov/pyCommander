# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 16:29:31 2023

@author: Yevhen_Vieskov
"""

# The Parent Class
from PyQt5.QtWidgets import  QWidget, QHBoxLayout,QLabel
class ParentWindow(QWidget):
    def __init__(self):
        super().__init__()
        title = "Main Window"
        self.setWindowTitle(title)
        left = 000; top = 500; width = 600; hight = 300
        self.setGeometry(left, top, width, hight)
        MainLayoutHbox = QHBoxLayout()
        header1 = QLabel("Header 1")
        header2 = QLabel("Header 2")
        header3 = QLabel("Header 3")
        MainLayoutHbox.addWidget(header1)
        MainLayoutHbox.addWidget(header2)
        MainLayoutHbox.addWidget(header3)
        self.setLayout(MainLayoutHbox)
# End of Parent Class


# The SubClass
# https://stackoverflow.com/questions/61340648/add-a-layout-to-another-layout-from-the-parent-window
from PyQt5.QtWidgets import QApplication,   QVBoxLayout, QHBoxLayout,  QTabWidget, QLabel
import sys

from ParentWindow import ParentWindow


class ChildWindow(ParentWindow):
    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout()
        MainLabel= QLabel("My Window")

        vbox.addWidget(MainLabel)

        self.layout().addLayout(vbox) # This show the Warning  Error

        # I assume the below code should work to extend the parent layout!! But it gives error
        # parent.MainLayoutHbox.addLayout(vbox)




if __name__ == "__main__":
    App = QApplication(sys.argv)
    MyWindow= ChildWindow()
    MyWindow.show()
    App.exec()