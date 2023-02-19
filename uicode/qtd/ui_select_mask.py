# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_maskZKcitj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogSelectMask(object):
    def setupUi(self, DialogSelectMask):
        if not DialogSelectMask.objectName():
            DialogSelectMask.setObjectName(u"DialogSelectMask")
        DialogSelectMask.resize(448, 448)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogSelectMask.sizePolicy().hasHeightForWidth())
        DialogSelectMask.setSizePolicy(sizePolicy)
        DialogSelectMask.setMinimumSize(QSize(448, 448))
        DialogSelectMask.setMaximumSize(QSize(448, 448))
        DialogSelectMask.setBaseSize(QSize(448, 448))
        DialogSelectMask.setModal(True)
        self.verticalLayout_2 = QVBoxLayout(DialogSelectMask)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelInputMask = QLabel(DialogSelectMask)
        self.labelInputMask.setObjectName(u"labelInputMask")

        self.verticalLayout_2.addWidget(self.labelInputMask)

        self.lineEditInputMask = QLineEdit(DialogSelectMask)
        self.lineEditInputMask.setObjectName(u"lineEditInputMask")

        self.verticalLayout_2.addWidget(self.lineEditInputMask)

        self.checkBoxCaseSensitive = QCheckBox(DialogSelectMask)
        self.checkBoxCaseSensitive.setObjectName(u"checkBoxCaseSensitive")

        self.verticalLayout_2.addWidget(self.checkBoxCaseSensitive)

        self.checkBoxIgnoreAccentsLigatures = QCheckBox(DialogSelectMask)
        self.checkBoxIgnoreAccentsLigatures.setObjectName(u"checkBoxIgnoreAccentsLigatures")

        self.verticalLayout_2.addWidget(self.checkBoxIgnoreAccentsLigatures)

        self.labelOrSelectPredefinedSelectionType = QLabel(DialogSelectMask)
        self.labelOrSelectPredefinedSelectionType.setObjectName(u"labelOrSelectPredefinedSelectionType")

        self.verticalLayout_2.addWidget(self.labelOrSelectPredefinedSelectionType)

        self.scrollAreaSelectMask = QScrollArea(DialogSelectMask)
        self.scrollAreaSelectMask.setObjectName(u"scrollAreaSelectMask")
        self.scrollAreaSelectMask.setWidgetResizable(True)
        self.scrollAreaWidgetSelectMask = QWidget()
        self.scrollAreaWidgetSelectMask.setObjectName(u"scrollAreaWidgetSelectMask")
        self.scrollAreaWidgetSelectMask.setGeometry(QRect(0, 0, 424, 258))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetSelectMask)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowserSelectMask = QTextBrowser(self.scrollAreaWidgetSelectMask)
        self.textBrowserSelectMask.setObjectName(u"textBrowserSelectMask")

        self.verticalLayout.addWidget(self.textBrowserSelectMask)

        self.scrollAreaSelectMask.setWidget(self.scrollAreaWidgetSelectMask)

        self.verticalLayout_2.addWidget(self.scrollAreaSelectMask)

        self.buttonBox = QDialogButtonBox(DialogSelectMask)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.labelInputMask.setBuddy(self.lineEditInputMask)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(DialogSelectMask)
        self.buttonBox.accepted.connect(DialogSelectMask.accept)
        self.buttonBox.rejected.connect(DialogSelectMask.reject)

        QMetaObject.connectSlotsByName(DialogSelectMask)
    # setupUi

    def retranslateUi(self, DialogSelectMask):
        DialogSelectMask.setWindowTitle(QCoreApplication.translate("DialogSelectMask", u"Select mask", None))
        self.labelInputMask.setText(QCoreApplication.translate("DialogSelectMask", u"Input mask:", None))
        self.lineEditInputMask.setText(QCoreApplication.translate("DialogSelectMask", u"*.*", None))
        self.checkBoxCaseSensitive.setText(QCoreApplication.translate("DialogSelectMask", u"Case sensitive", None))
        self.checkBoxIgnoreAccentsLigatures.setText(QCoreApplication.translate("DialogSelectMask", u"Ignore accents and ligatures", None))
        self.labelOrSelectPredefinedSelectionType.setText(QCoreApplication.translate("DialogSelectMask", u"Or select predefined selection type:", None))
    # retranslateUi

