# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 19:30:44 2023

@author: Yevhen_Vieskov
"""
#https://stackoverflow.com/questions/60495523/how-to-adjust-the-size-of-a-widget-within-a-horizontal-layout
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QGridLayout, QWidget, QListWidget, QLineEdit, QHBoxLayout, QPushButton


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        self.Search_Bar = QLineEdit(placeholderText="Search")
        self.Button = QPushButton('button')
        sp = self.Button.sizePolicy()
        sp.setHorizontalPolicy(QtWidgets.QSizePolicy.Fixed)
        self.Button.setSizePolicy(sp)
        layout = QHBoxLayout(centralWidget)
        layout.addWidget(self.Button)
        layout.addWidget(self.Search_Bar)
        layout.addWidget(self.Button, stretch=1)
        layout.addWidget(self.Search_Bar, stretch=1)
       


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())