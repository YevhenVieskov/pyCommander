# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 22:26:47 2023

@author: Yevhen_Vieskov
"""
from pathlib import  Path
import os
import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QToolBar,
    QAction,
    QStatusBar,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))

        # I also tried this, but it still doesn't work
        toolbar.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.addToolBar(toolbar)

        # @@@ Attach icon to QAction
        
        path = os.path.dirname(__file__)
        print(path)
        print(os.chdir(path))
        print(os.path.abspath(__file__))
        
        icon_path = str(Path(__file__).parent / "bug.png")
        print(icon_path)
        button_action = QAction(QIcon(icon_path), "Your button", self)
        #button_action = QAction(QIcon("bug.png"), "Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)
        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick(self, s):
        print("click", s)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()