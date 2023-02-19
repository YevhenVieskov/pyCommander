# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'linkerlgDyum.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogLinker(object):
    def setupUi(self, DialogLinker):
        if not DialogLinker.objectName():
            DialogLinker.setObjectName(u"DialogLinker")
        DialogLinker.resize(448, 448)
        DialogLinker.setMinimumSize(QSize(448, 448))
        DialogLinker.setMaximumSize(QSize(448, 448))
        DialogLinker.setBaseSize(QSize(448, 448))
        DialogLinker.setModal(True)
        self.gridLayout = QGridLayout(DialogLinker)
        self.gridLayout.setObjectName(u"gridLayout")
        self.textBrowserFileParts = QTextBrowser(DialogLinker)
        self.textBrowserFileParts.setObjectName(u"textBrowserFileParts")

        self.gridLayout.addWidget(self.textBrowserFileParts, 0, 0, 1, 1)

        self.groupBoxButtons = QGroupBox(DialogLinker)
        self.groupBoxButtons.setObjectName(u"groupBoxButtons")
        self.verticalLayout = QVBoxLayout(self.groupBoxButtons)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButtonUp = QPushButton(self.groupBoxButtons)
        self.pushButtonUp.setObjectName(u"pushButtonUp")

        self.verticalLayout.addWidget(self.pushButtonUp)

        self.pushButtonDown = QPushButton(self.groupBoxButtons)
        self.pushButtonDown.setObjectName(u"pushButtonDown")

        self.verticalLayout.addWidget(self.pushButtonDown)

        self.pushButtonRemove = QPushButton(self.groupBoxButtons)
        self.pushButtonRemove.setObjectName(u"pushButtonRemove")

        self.verticalLayout.addWidget(self.pushButtonRemove)

        self.verticalSpacerButtons = QSpacerItem(20, 143, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacerButtons)


        self.gridLayout.addWidget(self.groupBoxButtons, 0, 1, 1, 1)

        self.groupBoxSaveTo = QGroupBox(DialogLinker)
        self.groupBoxSaveTo.setObjectName(u"groupBoxSaveTo")
        self.verticalLayout_2 = QVBoxLayout(self.groupBoxSaveTo)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelSaveTo = QLabel(self.groupBoxSaveTo)
        self.labelSaveTo.setObjectName(u"labelSaveTo")

        self.verticalLayout_2.addWidget(self.labelSaveTo)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.lineEditSaveTo = QLineEdit(self.groupBoxSaveTo)
        self.lineEditSaveTo.setObjectName(u"lineEditSaveTo")

        self.horizontalLayout.addWidget(self.lineEditSaveTo)

        self.pushButtonSaveTo = QPushButton(self.groupBoxSaveTo)
        self.pushButtonSaveTo.setObjectName(u"pushButtonSaveTo")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSaveTo.sizePolicy().hasHeightForWidth())
        self.pushButtonSaveTo.setSizePolicy(sizePolicy)
        self.pushButtonSaveTo.setMinimumSize(QSize(32, 0))
        self.pushButtonSaveTo.setMaximumSize(QSize(32, 16777215))
        self.pushButtonSaveTo.setBaseSize(QSize(32, 0))
        self.pushButtonSaveTo.setFlat(False)

        self.horizontalLayout.addWidget(self.pushButtonSaveTo)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.gridLayout.addWidget(self.groupBoxSaveTo, 1, 0, 1, 2)

        self.buttonBox = QDialogButtonBox(DialogLinker)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)


        self.retranslateUi(DialogLinker)
        self.buttonBox.accepted.connect(DialogLinker.accept)
        self.buttonBox.rejected.connect(DialogLinker.reject)

        QMetaObject.connectSlotsByName(DialogLinker)
    # setupUi

    def retranslateUi(self, DialogLinker):
        DialogLinker.setWindowTitle(QCoreApplication.translate("DialogLinker", u"Linker", None))
        self.groupBoxButtons.setTitle(QCoreApplication.translate("DialogLinker", u"Item", None))
        self.pushButtonUp.setText(QCoreApplication.translate("DialogLinker", u"Up", None))
        self.pushButtonDown.setText(QCoreApplication.translate("DialogLinker", u"Down", None))
        self.pushButtonRemove.setText(QCoreApplication.translate("DialogLinker", u"Remove", None))
        self.groupBoxSaveTo.setTitle(QCoreApplication.translate("DialogLinker", u"Save to...", None))
        self.labelSaveTo.setText(QCoreApplication.translate("DialogLinker", u"File name", None))
        self.pushButtonSaveTo.setText(QCoreApplication.translate("DialogLinker", u"...", None))
    # retranslateUi

