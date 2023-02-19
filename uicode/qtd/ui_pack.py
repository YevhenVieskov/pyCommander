# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'packZCOuAE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PackFiles(object):
    def setupUi(self, PackFiles):
        if not PackFiles.objectName():
            PackFiles.setObjectName(u"PackFiles")
        PackFiles.setWindowModality(Qt.WindowModal)
        PackFiles.resize(768, 320)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PackFiles.sizePolicy().hasHeightForWidth())
        PackFiles.setSizePolicy(sizePolicy)
        PackFiles.setMinimumSize(QSize(768, 320))
        PackFiles.setMaximumSize(QSize(768, 320))
        PackFiles.setBaseSize(QSize(768, 320))
        PackFiles.setSizeGripEnabled(False)
        PackFiles.setModal(True)
        self.gridLayout_3 = QGridLayout(PackFiles)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(10)
        self.line = QFrame(PackFiles)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 1, 0, 1, 2)

        self.verticalLayoutPacker = QVBoxLayout()
        self.verticalLayoutPacker.setObjectName(u"verticalLayoutPacker")
        self.groupBoxArchiveType = QGroupBox(PackFiles)
        self.groupBoxArchiveType.setObjectName(u"groupBoxArchiveType")
        self.gridLayout_2 = QGridLayout(self.groupBoxArchiveType)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(5)
        self.radioButtonZip = QRadioButton(self.groupBoxArchiveType)
        self.radioButtonZip.setObjectName(u"radioButtonZip")

        self.gridLayout_2.addWidget(self.radioButtonZip, 0, 0, 1, 1)

        self.radioButtonTbz = QRadioButton(self.groupBoxArchiveType)
        self.radioButtonTbz.setObjectName(u"radioButtonTbz")

        self.gridLayout_2.addWidget(self.radioButtonTbz, 1, 1, 1, 1)

        self.radioButtonGz = QRadioButton(self.groupBoxArchiveType)
        self.radioButtonGz.setObjectName(u"radioButtonGz")

        self.gridLayout_2.addWidget(self.radioButtonGz, 0, 2, 1, 1)

        self.radioButtonTgz = QRadioButton(self.groupBoxArchiveType)
        self.radioButtonTgz.setObjectName(u"radioButtonTgz")

        self.gridLayout_2.addWidget(self.radioButtonTgz, 2, 0, 1, 1)

        self.radioButton7z = QRadioButton(self.groupBoxArchiveType)
        self.radioButton7z.setObjectName(u"radioButton7z")

        self.gridLayout_2.addWidget(self.radioButton7z, 0, 1, 1, 1)

        self.radioButtonLzma = QRadioButton(self.groupBoxArchiveType)
        self.radioButtonLzma.setObjectName(u"radioButtonLzma")

        self.gridLayout_2.addWidget(self.radioButtonLzma, 2, 1, 1, 1)

        self.radioButtonBz2 = QRadioButton(self.groupBoxArchiveType)
        self.radioButtonBz2.setObjectName(u"radioButtonBz2")

        self.gridLayout_2.addWidget(self.radioButtonBz2, 1, 0, 1, 1)

        self.radioButtonTar = QRadioButton(self.groupBoxArchiveType)
        self.radioButtonTar.setObjectName(u"radioButtonTar")

        self.gridLayout_2.addWidget(self.radioButtonTar, 1, 2, 1, 1)

        self.radioButtonTlz = QRadioButton(self.groupBoxArchiveType)
        self.radioButtonTlz.setObjectName(u"radioButtonTlz")

        self.gridLayout_2.addWidget(self.radioButtonTlz, 2, 2, 1, 1)


        self.verticalLayoutPacker.addWidget(self.groupBoxArchiveType)

        self.horizontalLayoutArchiveExtension = QHBoxLayout()
        self.horizontalLayoutArchiveExtension.setSpacing(7)
        self.horizontalLayoutArchiveExtension.setObjectName(u"horizontalLayoutArchiveExtension")
        self.horizontalLayoutArchiveExtension.setContentsMargins(10, -1, 10, -1)
        self.checkBoxChooseExtension = QCheckBox(PackFiles)
        self.checkBoxChooseExtension.setObjectName(u"checkBoxChooseExtension")

        self.horizontalLayoutArchiveExtension.addWidget(self.checkBoxChooseExtension)

        self.comboBoxArchiveExt = QComboBox(PackFiles)
        self.comboBoxArchiveExt.addItem("")
        self.comboBoxArchiveExt.addItem("")
        self.comboBoxArchiveExt.addItem("")
        self.comboBoxArchiveExt.addItem("")
        self.comboBoxArchiveExt.addItem("")
        self.comboBoxArchiveExt.addItem("")
        self.comboBoxArchiveExt.addItem("")
        self.comboBoxArchiveExt.setObjectName(u"comboBoxArchiveExt")

        self.horizontalLayoutArchiveExtension.addWidget(self.comboBoxArchiveExt)


        self.verticalLayoutPacker.addLayout(self.horizontalLayoutArchiveExtension)

        self.pushButtonConfigure = QPushButton(PackFiles)
        self.pushButtonConfigure.setObjectName(u"pushButtonConfigure")

        self.verticalLayoutPacker.addWidget(self.pushButtonConfigure)


        self.gridLayout_3.addLayout(self.verticalLayoutPacker, 0, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(PackFiles)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_3.addWidget(self.buttonBox, 2, 1, 1, 1)

        self.verticalLayoutPackFiles = QVBoxLayout()
        self.verticalLayoutPackFiles.setObjectName(u"verticalLayoutPackFiles")
        self.labelPackFileToFile = QLabel(PackFiles)
        self.labelPackFileToFile.setObjectName(u"labelPackFileToFile")

        self.verticalLayoutPackFiles.addWidget(self.labelPackFileToFile)

        self.horizontalLayoutPath = QHBoxLayout()
        self.horizontalLayoutPath.setObjectName(u"horizontalLayoutPath")
        self.lineEditFileName = QLineEdit(PackFiles)
        self.lineEditFileName.setObjectName(u"lineEditFileName")

        self.horizontalLayoutPath.addWidget(self.lineEditFileName)

        self.pushButton = QPushButton(PackFiles)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u"../pyCommander/pixmaps/dctheme/16x16/actions/cm_changedirtoroot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)

        self.horizontalLayoutPath.addWidget(self.pushButton)


        self.verticalLayoutPackFiles.addLayout(self.horizontalLayoutPath)

        self.checkBoxAlsoPackNames = QCheckBox(PackFiles)
        self.checkBoxAlsoPackNames.setObjectName(u"checkBoxAlsoPackNames")
        self.checkBoxAlsoPackNames.setChecked(True)

        self.verticalLayoutPackFiles.addWidget(self.checkBoxAlsoPackNames)

        self.checkBoxMultipleDiskArchive = QCheckBox(PackFiles)
        self.checkBoxMultipleDiskArchive.setObjectName(u"checkBoxMultipleDiskArchive")

        self.verticalLayoutPackFiles.addWidget(self.checkBoxMultipleDiskArchive)

        self.checkBoxMoveToArchive = QCheckBox(PackFiles)
        self.checkBoxMoveToArchive.setObjectName(u"checkBoxMoveToArchive")

        self.verticalLayoutPackFiles.addWidget(self.checkBoxMoveToArchive)

        self.checkBoxCreateSelfExtractArchive = QCheckBox(PackFiles)
        self.checkBoxCreateSelfExtractArchive.setObjectName(u"checkBoxCreateSelfExtractArchive")

        self.verticalLayoutPackFiles.addWidget(self.checkBoxCreateSelfExtractArchive)

        self.checkBoxEncrypt = QCheckBox(PackFiles)
        self.checkBoxEncrypt.setObjectName(u"checkBoxEncrypt")

        self.verticalLayoutPackFiles.addWidget(self.checkBoxEncrypt)

        self.checkBoxPutInTarArchiveFirst = QCheckBox(PackFiles)
        self.checkBoxPutInTarArchiveFirst.setObjectName(u"checkBoxPutInTarArchiveFirst")

        self.verticalLayoutPackFiles.addWidget(self.checkBoxPutInTarArchiveFirst)

        self.checkBoxCreateSeparateArchive = QCheckBox(PackFiles)
        self.checkBoxCreateSeparateArchive.setObjectName(u"checkBoxCreateSeparateArchive")

        self.verticalLayoutPackFiles.addWidget(self.checkBoxCreateSeparateArchive)


        self.gridLayout_3.addLayout(self.verticalLayoutPackFiles, 0, 0, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 2)
#if QT_CONFIG(shortcut)
        self.labelPackFileToFile.setBuddy(self.lineEditFileName)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.lineEditFileName, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.checkBoxAlsoPackNames)
        QWidget.setTabOrder(self.checkBoxAlsoPackNames, self.checkBoxMultipleDiskArchive)
        QWidget.setTabOrder(self.checkBoxMultipleDiskArchive, self.checkBoxMoveToArchive)
        QWidget.setTabOrder(self.checkBoxMoveToArchive, self.checkBoxCreateSelfExtractArchive)
        QWidget.setTabOrder(self.checkBoxCreateSelfExtractArchive, self.checkBoxEncrypt)
        QWidget.setTabOrder(self.checkBoxEncrypt, self.checkBoxPutInTarArchiveFirst)
        QWidget.setTabOrder(self.checkBoxPutInTarArchiveFirst, self.checkBoxCreateSeparateArchive)
        QWidget.setTabOrder(self.checkBoxCreateSeparateArchive, self.radioButtonZip)
        QWidget.setTabOrder(self.radioButtonZip, self.radioButton7z)
        QWidget.setTabOrder(self.radioButton7z, self.radioButtonGz)
        QWidget.setTabOrder(self.radioButtonGz, self.radioButtonBz2)
        QWidget.setTabOrder(self.radioButtonBz2, self.radioButtonTbz)
        QWidget.setTabOrder(self.radioButtonTbz, self.radioButtonTar)
        QWidget.setTabOrder(self.radioButtonTar, self.radioButtonTgz)
        QWidget.setTabOrder(self.radioButtonTgz, self.radioButtonLzma)
        QWidget.setTabOrder(self.radioButtonLzma, self.radioButtonTlz)
        QWidget.setTabOrder(self.radioButtonTlz, self.checkBoxChooseExtension)
        QWidget.setTabOrder(self.checkBoxChooseExtension, self.comboBoxArchiveExt)
        QWidget.setTabOrder(self.comboBoxArchiveExt, self.pushButtonConfigure)

        self.retranslateUi(PackFiles)
        self.buttonBox.accepted.connect(PackFiles.accept)
        self.buttonBox.rejected.connect(PackFiles.reject)
        self.checkBoxChooseExtension.clicked.connect(self.comboBoxArchiveExt.setFocus)

        QMetaObject.connectSlotsByName(PackFiles)
    # setupUi

    def retranslateUi(self, PackFiles):
        PackFiles.setWindowTitle(QCoreApplication.translate("PackFiles", u"Pack file(s)", None))
        self.groupBoxArchiveType.setTitle(QCoreApplication.translate("PackFiles", u"Packer", None))
        self.radioButtonZip.setText(QCoreApplication.translate("PackFiles", u"zip", None))
        self.radioButtonTbz.setText(QCoreApplication.translate("PackFiles", u"tbz", None))
        self.radioButtonGz.setText(QCoreApplication.translate("PackFiles", u"gz", None))
        self.radioButtonTgz.setText(QCoreApplication.translate("PackFiles", u"tgz", None))
        self.radioButton7z.setText(QCoreApplication.translate("PackFiles", u"7z", None))
        self.radioButtonLzma.setText(QCoreApplication.translate("PackFiles", u"lzma", None))
        self.radioButtonBz2.setText(QCoreApplication.translate("PackFiles", u"bz2", None))
        self.radioButtonTar.setText(QCoreApplication.translate("PackFiles", u"tar", None))
        self.radioButtonTlz.setText(QCoreApplication.translate("PackFiles", u"tlz", None))
        self.checkBoxChooseExtension.setText(QCoreApplication.translate("PackFiles", u"=>", None))
        self.comboBoxArchiveExt.setItemText(0, QCoreApplication.translate("PackFiles", u"xz", None))
        self.comboBoxArchiveExt.setItemText(1, QCoreApplication.translate("PackFiles", u"zst", None))
        self.comboBoxArchiveExt.setItemText(2, QCoreApplication.translate("PackFiles", u"txz", None))
        self.comboBoxArchiveExt.setItemText(3, QCoreApplication.translate("PackFiles", u"zipx", None))
        self.comboBoxArchiveExt.setItemText(4, QCoreApplication.translate("PackFiles", u"wim", None))
        self.comboBoxArchiveExt.setItemText(5, QCoreApplication.translate("PackFiles", u"rar", None))
        self.comboBoxArchiveExt.setItemText(6, QCoreApplication.translate("PackFiles", u"txz", None))

        self.pushButtonConfigure.setText(QCoreApplication.translate("PackFiles", u"Configure", None))
        self.labelPackFileToFile.setText(QCoreApplication.translate("PackFiles", u"Pack file(s) to the file:", None))
        self.pushButton.setText("")
        self.checkBoxAlsoPackNames.setText(QCoreApplication.translate("PackFiles", u"Also pack path names (only recursed)", None))
        self.checkBoxMultipleDiskArchive.setText(QCoreApplication.translate("PackFiles", u"Multiple disk archive", None))
        self.checkBoxMoveToArchive.setText(QCoreApplication.translate("PackFiles", u"Move to archive", None))
        self.checkBoxCreateSelfExtractArchive.setText(QCoreApplication.translate("PackFiles", u"Create self extracting archive", None))
        self.checkBoxEncrypt.setText(QCoreApplication.translate("PackFiles", u"Encrypt", None))
        self.checkBoxPutInTarArchiveFirst.setText(QCoreApplication.translate("PackFiles", u"Put in the TAR archive first", None))
        self.checkBoxCreateSeparateArchive.setText(QCoreApplication.translate("PackFiles", u"Create separate archives, one per selected file/dir", None))
    # retranslateUi

