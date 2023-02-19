# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'linker.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogLinker(object):
    def setupUi(self, DialogLinker):
        DialogLinker.setObjectName("DialogLinker")
        DialogLinker.resize(448, 448)
        DialogLinker.setMinimumSize(QtCore.QSize(448, 448))
        DialogLinker.setMaximumSize(QtCore.QSize(448, 448))
        DialogLinker.setBaseSize(QtCore.QSize(448, 448))
        DialogLinker.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(DialogLinker)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowserFileParts = QtWidgets.QTextBrowser(DialogLinker)
        self.textBrowserFileParts.setObjectName("textBrowserFileParts")
        self.gridLayout.addWidget(self.textBrowserFileParts, 0, 0, 1, 1)
        self.groupBoxButtons = QtWidgets.QGroupBox(DialogLinker)
        self.groupBoxButtons.setObjectName("groupBoxButtons")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBoxButtons)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonUp = QtWidgets.QPushButton(self.groupBoxButtons)
        self.pushButtonUp.setObjectName("pushButtonUp")
        self.verticalLayout.addWidget(self.pushButtonUp)
        self.pushButtonDown = QtWidgets.QPushButton(self.groupBoxButtons)
        self.pushButtonDown.setObjectName("pushButtonDown")
        self.verticalLayout.addWidget(self.pushButtonDown)
        self.pushButtonRemove = QtWidgets.QPushButton(self.groupBoxButtons)
        self.pushButtonRemove.setObjectName("pushButtonRemove")
        self.verticalLayout.addWidget(self.pushButtonRemove)
        spacerItem = QtWidgets.QSpacerItem(20, 143, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addWidget(self.groupBoxButtons, 0, 1, 1, 1)
        self.groupBoxSaveTo = QtWidgets.QGroupBox(DialogLinker)
        self.groupBoxSaveTo.setObjectName("groupBoxSaveTo")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBoxSaveTo)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelSaveTo = QtWidgets.QLabel(self.groupBoxSaveTo)
        self.labelSaveTo.setObjectName("labelSaveTo")
        self.verticalLayout_2.addWidget(self.labelSaveTo)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditSaveTo = QtWidgets.QLineEdit(self.groupBoxSaveTo)
        self.lineEditSaveTo.setObjectName("lineEditSaveTo")
        self.horizontalLayout.addWidget(self.lineEditSaveTo)
        self.pushButtonSaveTo = QtWidgets.QPushButton(self.groupBoxSaveTo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSaveTo.sizePolicy().hasHeightForWidth())
        self.pushButtonSaveTo.setSizePolicy(sizePolicy)
        self.pushButtonSaveTo.setMinimumSize(QtCore.QSize(32, 0))
        self.pushButtonSaveTo.setMaximumSize(QtCore.QSize(32, 16777215))
        self.pushButtonSaveTo.setBaseSize(QtCore.QSize(32, 0))
        self.pushButtonSaveTo.setFlat(False)
        self.pushButtonSaveTo.setObjectName("pushButtonSaveTo")
        self.horizontalLayout.addWidget(self.pushButtonSaveTo)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addWidget(self.groupBoxSaveTo, 1, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogLinker)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)

        self.retranslateUi(DialogLinker)
        self.buttonBox.accepted.connect(DialogLinker.accept) # type: ignore
        self.buttonBox.rejected.connect(DialogLinker.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DialogLinker)

    def retranslateUi(self, DialogLinker):
        _translate = QtCore.QCoreApplication.translate
        DialogLinker.setWindowTitle(_translate("DialogLinker", "Linker"))
        self.groupBoxButtons.setTitle(_translate("DialogLinker", "Item"))
        self.pushButtonUp.setText(_translate("DialogLinker", "Up"))
        self.pushButtonDown.setText(_translate("DialogLinker", "Down"))
        self.pushButtonRemove.setText(_translate("DialogLinker", "Remove"))
        self.groupBoxSaveTo.setTitle(_translate("DialogLinker", "Save to..."))
        self.labelSaveTo.setText(_translate("DialogLinker", "File name"))
        self.pushButtonSaveTo.setText(_translate("DialogLinker", "..."))
