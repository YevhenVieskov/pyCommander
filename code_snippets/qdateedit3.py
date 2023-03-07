# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 09:41:29 2023

@author: Yevhen_Vieskov
"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
 
app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(400,400,250,250)
win.setWindowTitle("CodersLegacy")
 
date = QtWidgets.QDateEdit(win)
date.setMinimumDate(QDate(1900, 1, 1))
date.setMaximumDate(QDate(2100, 12, 31))
date.move(50,50)
 
win.show()
sys.exit(app.exec_())