# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 19:08:25 2023

@author: Yevhen_Vieskov
"""

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(600, 400))
        self.move(600, 300)
        self.setWindowTitle('Horizontal Layout')

        self.container = QWidget()
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)

        self.button_1 = QPushButton('Button 1')
        self.button_1.setFixedSize(QSize(70, 60))
        self.button_2 = QPushButton('Button 2')
        self.button_2.setFixedSize(QSize(70, 60))
        self.button_3 = QPushButton('Button 3')
        self.button_3.setFixedSize(QSize(70, 60))
        self.button_4 = QPushButton('Button 4')
        self.button_4.setFixedSize(QSize(70, 60))
        self.button_5 = QPushButton('Button 5')
        self.button_5.setFixedSize(QSize(70, 60))
        self.button_6 = QPushButton('Button 6')
        self.button_6.setFixedSize(QSize(70, 60))
        self.button_7 = QPushButton('Button 7')
        self.button_7.setFixedSize(QSize(70, 60))

        self.horizontalLayout.addWidget(self.button_1)
        self.horizontalLayout.addWidget(self.button_2)
        self.horizontalLayout.addWidget(self.button_3)
        self.horizontalLayout.addStretch()
        self.horizontalLayout.addWidget(self.button_4)
        self.horizontalLayout.addWidget(self.button_5)
        self.horizontalLayout.addStretch()
        self.horizontalLayout.addWidget(self.button_6)
        self.horizontalLayout.addWidget(self.button_7)

        self.setLayout(self.horizontalLayout)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()