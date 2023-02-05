# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 16:03:58 2023

@author: Yevhen_Vieskov
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Ornek(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.toggles = []
        lay = QVBoxLayout(self)
        h_box = QGridLayout()
        lay.addLayout(h_box)

        for i in range(4):
            btngroup = QButtonGroup(self)
            btngroup.buttonClicked.connect(lambda btn: print(btn.text()))

            for j in range(4):
                btn = QRadioButton()
                btngroup.addButton(btn)
                h_box.addWidget(btn, i, j, 1, 1)

                if j % 4 == 0:
                    btn.setText("A")
                elif j % 4 == 1:
                    btn.setText("B")
                elif j % 4 == 2:
                    btn.setText("C")
                else:
                    btn.setText("D")

        
        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle("Çıkış Projesi")
        self.show()



        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pencere = Ornek()
    sys.exit(app.exec_())