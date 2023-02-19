# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splittertwQPLn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Splitter(object):
    def setupUi(self, Splitter):
        if not Splitter.objectName():
            Splitter.setObjectName(u"Splitter")
        Splitter.resize(576, 320)
        Splitter.setMinimumSize(QSize(576, 320))
        Splitter.setMaximumSize(QSize(576, 320))
        Splitter.setBaseSize(QSize(576, 320))
        Splitter.setModal(True)
        self.verticalLayout_2 = QVBoxLayout(Splitter)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(Splitter)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayoutSplitTheFileToDirectory = QHBoxLayout()
        self.horizontalLayoutSplitTheFileToDirectory.setObjectName(u"horizontalLayoutSplitTheFileToDirectory")
        self.lineEditSplitTheFileToDirectory = QLineEdit(Splitter)
        self.lineEditSplitTheFileToDirectory.setObjectName(u"lineEditSplitTheFileToDirectory")

        self.horizontalLayoutSplitTheFileToDirectory.addWidget(self.lineEditSplitTheFileToDirectory)

        self.pushButtonOpenFolder = QPushButton(Splitter)
        self.pushButtonOpenFolder.setObjectName(u"pushButtonOpenFolder")
        icon = QIcon()
        icon.addFile(u"../pyCommander/pixmaps/dctheme/16x16/actions/cm_changedirtoroot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonOpenFolder.setIcon(icon)

        self.horizontalLayoutSplitTheFileToDirectory.addWidget(self.pushButtonOpenFolder)

        self.pushButtonSettings = QPushButton(Splitter)
        self.pushButtonSettings.setObjectName(u"pushButtonSettings")
        icon1 = QIcon()
        icon1.addFile(u"../pyCommander/pixmaps/dctheme/16x16/actions/mr-pathtools.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonSettings.setIcon(icon1)

        self.horizontalLayoutSplitTheFileToDirectory.addWidget(self.pushButtonSettings)


        self.verticalLayout_2.addLayout(self.horizontalLayoutSplitTheFileToDirectory)

        self.groupBoxSizeAndNumberOfParts = QGroupBox(Splitter)
        self.groupBoxSizeAndNumberOfParts.setObjectName(u"groupBoxSizeAndNumberOfParts")
        self.verticalLayout = QVBoxLayout(self.groupBoxSizeAndNumberOfParts)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 200, -1)
        self.comboBoxSizeAndNumberOfParts = QComboBox(self.groupBoxSizeAndNumberOfParts)
        self.comboBoxSizeAndNumberOfParts.addItem("")
        self.comboBoxSizeAndNumberOfParts.addItem("")
        self.comboBoxSizeAndNumberOfParts.addItem("")
        self.comboBoxSizeAndNumberOfParts.addItem("")
        self.comboBoxSizeAndNumberOfParts.addItem("")
        self.comboBoxSizeAndNumberOfParts.addItem("")
        self.comboBoxSizeAndNumberOfParts.addItem("")
        self.comboBoxSizeAndNumberOfParts.addItem("")
        self.comboBoxSizeAndNumberOfParts.addItem("")
        self.comboBoxSizeAndNumberOfParts.setObjectName(u"comboBoxSizeAndNumberOfParts")
        self.comboBoxSizeAndNumberOfParts.setEditable(False)

        self.verticalLayout.addWidget(self.comboBoxSizeAndNumberOfParts)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButtonBytes = QRadioButton(self.groupBoxSizeAndNumberOfParts)
        self.radioButtonBytes.setObjectName(u"radioButtonBytes")
        self.radioButtonBytes.setChecked(True)

        self.horizontalLayout.addWidget(self.radioButtonBytes)

        self.radioButtonKilobytes = QRadioButton(self.groupBoxSizeAndNumberOfParts)
        self.radioButtonKilobytes.setObjectName(u"radioButtonKilobytes")

        self.horizontalLayout.addWidget(self.radioButtonKilobytes)

        self.radioButtonMegabytes = QRadioButton(self.groupBoxSizeAndNumberOfParts)
        self.radioButtonMegabytes.setObjectName(u"radioButtonMegabytes")

        self.horizontalLayout.addWidget(self.radioButtonMegabytes)

        self.radioButtonGigabytes = QRadioButton(self.groupBoxSizeAndNumberOfParts)
        self.radioButtonGigabytes.setObjectName(u"radioButtonGigabytes")

        self.horizontalLayout.addWidget(self.radioButtonGigabytes)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayoutNumbersOfPart = QHBoxLayout()
        self.horizontalLayoutNumbersOfPart.setSpacing(7)
        self.horizontalLayoutNumbersOfPart.setObjectName(u"horizontalLayoutNumbersOfPart")
        self.horizontalLayoutNumbersOfPart.setContentsMargins(-1, -1, 50, -1)
        self.labelNumberOfParts = QLabel(self.groupBoxSizeAndNumberOfParts)
        self.labelNumberOfParts.setObjectName(u"labelNumberOfParts")

        self.horizontalLayoutNumbersOfPart.addWidget(self.labelNumberOfParts)

        self.lineEditNumberOfParts = QLineEdit(self.groupBoxSizeAndNumberOfParts)
        self.lineEditNumberOfParts.setObjectName(u"lineEditNumberOfParts")

        self.horizontalLayoutNumbersOfPart.addWidget(self.lineEditNumberOfParts)


        self.verticalLayout.addLayout(self.horizontalLayoutNumbersOfPart)

        self.checkBoxRequireCR32 = QCheckBox(self.groupBoxSizeAndNumberOfParts)
        self.checkBoxRequireCR32.setObjectName(u"checkBoxRequireCR32")

        self.verticalLayout.addWidget(self.checkBoxRequireCR32)


        self.verticalLayout_2.addWidget(self.groupBoxSizeAndNumberOfParts)

        self.buttonBox = QDialogButtonBox(Splitter)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)

        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 4)
        self.verticalLayout_2.setStretch(3, 1)
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.lineEditSplitTheFileToDirectory)
        self.labelNumberOfParts.setBuddy(self.lineEditNumberOfParts)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Splitter)
        self.buttonBox.accepted.connect(Splitter.accept)
        self.buttonBox.rejected.connect(Splitter.reject)

        QMetaObject.connectSlotsByName(Splitter)
    # setupUi

    def retranslateUi(self, Splitter):
        Splitter.setWindowTitle(QCoreApplication.translate("Splitter", u"Splitter", None))
        self.label.setText(QCoreApplication.translate("Splitter", u"Split the file to directory:", None))
        self.pushButtonOpenFolder.setText("")
        self.pushButtonSettings.setText("")
        self.groupBoxSizeAndNumberOfParts.setTitle(QCoreApplication.translate("Splitter", u"Size and number of parts", None))
        self.comboBoxSizeAndNumberOfParts.setItemText(0, QCoreApplication.translate("Splitter", u"Automatic", None))
        self.comboBoxSizeAndNumberOfParts.setItemText(1, QCoreApplication.translate("Splitter", u"1457664B - 3.5\" High Density 1.44M", None))
        self.comboBoxSizeAndNumberOfParts.setItemText(2, QCoreApplication.translate("Splitter", u"1213952B - 5.25\" High Density 1.2M", None))
        self.comboBoxSizeAndNumberOfParts.setItemText(3, QCoreApplication.translate("Splitter", u"730112B - 3.5\" Double Density 720K", None))
        self.comboBoxSizeAndNumberOfParts.setItemText(4, QCoreApplication.translate("Splitter", u"362496B - 5.25\" Double Density 360K", None))
        self.comboBoxSizeAndNumberOfParts.setItemText(5, QCoreApplication.translate("Splitter", u"98078KB - ZIP 100MB", None))
        self.comboBoxSizeAndNumberOfParts.setItemText(6, QCoreApplication.translate("Splitter", u"650MB - CD 650MB", None))
        self.comboBoxSizeAndNumberOfParts.setItemText(7, QCoreApplication.translate("Splitter", u"700MB - CD 700MB", None))
        self.comboBoxSizeAndNumberOfParts.setItemText(8, QCoreApplication.translate("Splitter", u"4482MB - DVD+R", None))

        self.radioButtonBytes.setText(QCoreApplication.translate("Splitter", u"Bytes", None))
        self.radioButtonKilobytes.setText(QCoreApplication.translate("Splitter", u"Kilobytes", None))
        self.radioButtonMegabytes.setText(QCoreApplication.translate("Splitter", u"Megabytes", None))
        self.radioButtonGigabytes.setText(QCoreApplication.translate("Splitter", u"Gigabytes", None))
        self.labelNumberOfParts.setText(QCoreApplication.translate("Splitter", u"Number of parts", None))
        self.checkBoxRequireCR32.setText(QCoreApplication.translate("Splitter", u"Require a CR32 verification file", None))
    # retranslateUi

