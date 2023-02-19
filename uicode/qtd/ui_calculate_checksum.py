# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculate_checksumCLQmHz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogCalculateChecksum(object):
    def setupUi(self, DialogCalculateChecksum):
        if not DialogCalculateChecksum.objectName():
            DialogCalculateChecksum.setObjectName(u"DialogCalculateChecksum")
        DialogCalculateChecksum.resize(448, 448)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogCalculateChecksum.sizePolicy().hasHeightForWidth())
        DialogCalculateChecksum.setSizePolicy(sizePolicy)
        DialogCalculateChecksum.setMinimumSize(QSize(448, 448))
        DialogCalculateChecksum.setMaximumSize(QSize(448, 448))
        DialogCalculateChecksum.setBaseSize(QSize(448, 448))
        DialogCalculateChecksum.setModal(True)
        self.verticalLayout_2 = QVBoxLayout(DialogCalculateChecksum)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelSaveChecksumFileTo = QLabel(DialogCalculateChecksum)
        self.labelSaveChecksumFileTo.setObjectName(u"labelSaveChecksumFileTo")

        self.verticalLayout_2.addWidget(self.labelSaveChecksumFileTo)

        self.lineEditSaveChecksumFileTo = QLineEdit(DialogCalculateChecksum)
        self.lineEditSaveChecksumFileTo.setObjectName(u"lineEditSaveChecksumFileTo")

        self.verticalLayout_2.addWidget(self.lineEditSaveChecksumFileTo)

        self.checkBoxCreateSeparateChecksumFile = QCheckBox(DialogCalculateChecksum)
        self.checkBoxCreateSeparateChecksumFile.setObjectName(u"checkBoxCreateSeparateChecksumFile")

        self.verticalLayout_2.addWidget(self.checkBoxCreateSeparateChecksumFile)

        self.checkBoxOpenChecksumFile = QCheckBox(DialogCalculateChecksum)
        self.checkBoxOpenChecksumFile.setObjectName(u"checkBoxOpenChecksumFile")

        self.verticalLayout_2.addWidget(self.checkBoxOpenChecksumFile)

        self.scrollAreaCheckSum = QScrollArea(DialogCalculateChecksum)
        self.scrollAreaCheckSum.setObjectName(u"scrollAreaCheckSum")
        self.scrollAreaCheckSum.setWidgetResizable(True)
        self.scrollAreaWidgetContentsCheckSum = QWidget()
        self.scrollAreaWidgetContentsCheckSum.setObjectName(u"scrollAreaWidgetContentsCheckSum")
        self.scrollAreaWidgetContentsCheckSum.setGeometry(QRect(0, 0, 424, 281))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContentsCheckSum)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowserCheckSum = QTextBrowser(self.scrollAreaWidgetContentsCheckSum)
        self.textBrowserCheckSum.setObjectName(u"textBrowserCheckSum")

        self.verticalLayout.addWidget(self.textBrowserCheckSum)

        self.scrollAreaCheckSum.setWidget(self.scrollAreaWidgetContentsCheckSum)

        self.verticalLayout_2.addWidget(self.scrollAreaCheckSum)

        self.buttonBox = QDialogButtonBox(DialogCalculateChecksum)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.labelSaveChecksumFileTo.setBuddy(self.lineEditSaveChecksumFileTo)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(DialogCalculateChecksum)
        self.buttonBox.accepted.connect(DialogCalculateChecksum.accept)
        self.buttonBox.rejected.connect(DialogCalculateChecksum.reject)

        QMetaObject.connectSlotsByName(DialogCalculateChecksum)
    # setupUi

    def retranslateUi(self, DialogCalculateChecksum):
        DialogCalculateChecksum.setWindowTitle(QCoreApplication.translate("DialogCalculateChecksum", u"Calculate checksum...", None))
        self.labelSaveChecksumFileTo.setText(QCoreApplication.translate("DialogCalculateChecksum", u"Save checksum file(s) to:", None))
        self.checkBoxCreateSeparateChecksumFile.setText(QCoreApplication.translate("DialogCalculateChecksum", u"Create separate checksum file for each file", None))
        self.checkBoxOpenChecksumFile.setText(QCoreApplication.translate("DialogCalculateChecksum", u"Open checksum file after job is completed", None))
    # retranslateUi

