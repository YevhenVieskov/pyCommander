# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_mask.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogSelectMask(object):
    def setupUi(self, DialogSelectMask):
        DialogSelectMask.setObjectName("DialogSelectMask")
        DialogSelectMask.resize(448, 448)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogSelectMask.sizePolicy().hasHeightForWidth())
        DialogSelectMask.setSizePolicy(sizePolicy)
        DialogSelectMask.setMinimumSize(QtCore.QSize(448, 448))
        DialogSelectMask.setMaximumSize(QtCore.QSize(448, 448))
        DialogSelectMask.setBaseSize(QtCore.QSize(448, 448))
        DialogSelectMask.setModal(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(DialogSelectMask)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelInputMask = QtWidgets.QLabel(DialogSelectMask)
        self.labelInputMask.setObjectName("labelInputMask")
        self.verticalLayout_2.addWidget(self.labelInputMask)
        self.lineEditInputMask = QtWidgets.QLineEdit(DialogSelectMask)
        self.lineEditInputMask.setObjectName("lineEditInputMask")
        self.verticalLayout_2.addWidget(self.lineEditInputMask)
        self.checkBoxCaseSensitive = QtWidgets.QCheckBox(DialogSelectMask)
        self.checkBoxCaseSensitive.setObjectName("checkBoxCaseSensitive")
        self.verticalLayout_2.addWidget(self.checkBoxCaseSensitive)
        self.checkBoxIgnoreAccentsLigatures = QtWidgets.QCheckBox(DialogSelectMask)
        self.checkBoxIgnoreAccentsLigatures.setObjectName("checkBoxIgnoreAccentsLigatures")
        self.verticalLayout_2.addWidget(self.checkBoxIgnoreAccentsLigatures)
        self.labelOrSelectPredefinedSelectionType = QtWidgets.QLabel(DialogSelectMask)
        self.labelOrSelectPredefinedSelectionType.setObjectName("labelOrSelectPredefinedSelectionType")
        self.verticalLayout_2.addWidget(self.labelOrSelectPredefinedSelectionType)
        self.scrollAreaSelectMask = QtWidgets.QScrollArea(DialogSelectMask)
        self.scrollAreaSelectMask.setWidgetResizable(True)
        self.scrollAreaSelectMask.setObjectName("scrollAreaSelectMask")
        self.scrollAreaWidgetSelectMask = QtWidgets.QWidget()
        self.scrollAreaWidgetSelectMask.setGeometry(QtCore.QRect(0, 0, 424, 258))
        self.scrollAreaWidgetSelectMask.setObjectName("scrollAreaWidgetSelectMask")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetSelectMask)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowserSelectMask = QtWidgets.QTextBrowser(self.scrollAreaWidgetSelectMask)
        self.textBrowserSelectMask.setObjectName("textBrowserSelectMask")
        self.verticalLayout.addWidget(self.textBrowserSelectMask)
        self.scrollAreaSelectMask.setWidget(self.scrollAreaWidgetSelectMask)
        self.verticalLayout_2.addWidget(self.scrollAreaSelectMask)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogSelectMask)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.labelInputMask.setBuddy(self.lineEditInputMask)

        self.retranslateUi(DialogSelectMask)
        self.buttonBox.accepted.connect(DialogSelectMask.accept) # type: ignore
        self.buttonBox.rejected.connect(DialogSelectMask.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DialogSelectMask)

    def retranslateUi(self, DialogSelectMask):
        _translate = QtCore.QCoreApplication.translate
        DialogSelectMask.setWindowTitle(_translate("DialogSelectMask", "Select mask"))
        self.labelInputMask.setText(_translate("DialogSelectMask", "Input mask:"))
        self.lineEditInputMask.setText(_translate("DialogSelectMask", "*.*"))
        self.checkBoxCaseSensitive.setText(_translate("DialogSelectMask", "Case sensitive"))
        self.checkBoxIgnoreAccentsLigatures.setText(_translate("DialogSelectMask", "Ignore accents and ligatures"))
        self.labelOrSelectPredefinedSelectionType.setText(_translate("DialogSelectMask", "Or select predefined selection type:"))
