# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 09:42:34 2023

@author: Yevhen_Vieskov
"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QDate
import sys
 
def display():
    print(date.date().toPyDate())
 
app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(400,400,250,250)
win.setWindowTitle("CodersLegacy")
 
date = QtWidgets.QDateEdit(win)
date.setMinimumDate(QDate(1900, 1, 1))
date.setMaximumDate(QDate(2100, 12, 31))
date.move(50,50)
 
button = QtWidgets.QPushButton(win)
button.setText("Press me")
button.clicked.connect(display)
button.move(50,100)
 
win.show()
sys.exit(app.exec_())