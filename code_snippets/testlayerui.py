# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 19:22:49 2023

@author: Yevhen_Vieskov
"""

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testKairuT.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(959, 292)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(12, 12, 551, 34))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButtonLeft = QPushButton(self.widget)
        self.pushButtonLeft.setObjectName(u"pushButtonLeft")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.pushButtonLeft.sizePolicy().hasHeightForWidth())
        self.pushButtonLeft.setSizePolicy(sizePolicy)
        self.pushButtonLeft.setMinimumSize(QSize(64, 32))
        self.pushButtonLeft.setBaseSize(QSize(64, 32))

        self.horizontalLayout.addWidget(self.pushButtonLeft)

        self.horizontalSpacerLeft = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacerLeft)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacerRight = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacerRight)

        self.pushButtonStar = QPushButton(self.widget)
        self.pushButtonStar.setObjectName(u"pushButtonStar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(32)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButtonStar.sizePolicy().hasHeightForWidth())
        self.pushButtonStar.setSizePolicy(sizePolicy1)
        self.pushButtonStar.setMinimumSize(QSize(32, 32))
        self.pushButtonStar.setBaseSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.pushButtonStar)

        self.pushButtonSlash = QPushButton(self.widget)
        self.pushButtonSlash.setObjectName(u"pushButtonSlash")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButtonSlash.sizePolicy().hasHeightForWidth())
        self.pushButtonSlash.setSizePolicy(sizePolicy2)
        self.pushButtonSlash.setMinimumSize(QSize(32, 32))
        self.pushButtonSlash.setBaseSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.pushButtonSlash)

        self.pushButtonTwoPoint = QPushButton(self.widget)
        self.pushButtonTwoPoint.setObjectName(u"pushButtonTwoPoint")
        sizePolicy1.setHeightForWidth(self.pushButtonTwoPoint.sizePolicy().hasHeightForWidth())
        self.pushButtonTwoPoint.setSizePolicy(sizePolicy1)
        self.pushButtonTwoPoint.setMinimumSize(QSize(32, 32))
        self.pushButtonTwoPoint.setBaseSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.pushButtonTwoPoint)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 959, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButtonLeft.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButtonStar.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.pushButtonSlash.setText(QCoreApplication.translate("MainWindow", u"\\", None))
        self.pushButtonTwoPoint.setText(QCoreApplication.translate("MainWindow", u"..", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

