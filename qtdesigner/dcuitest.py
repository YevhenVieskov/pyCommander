# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 10:41:28 2023

@author: Yevhen_Vieskov
"""

from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('doublecommander.ui', self)
        self.show()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
