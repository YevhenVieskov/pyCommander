# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 18:34:08 2023

@author: Yevhen_Vieskov
"""
#https://stackoverflow.com/questions/42046092/how-do-i-create-a-signal-to-open-a-qfiledialog-in-qt-designer
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import uic
import sys


form_class = uic.loadUiType("mainWindow.ui")[0]  # Load the UI

class MyWindowClass(QMainWindow, form_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

    def mybutton_clicked(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*)", options=options)
        if fileName:
            print(fileName)

app = QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()