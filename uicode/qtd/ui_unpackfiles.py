# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'unpackfilesfKGCCO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(576, 320)
        Dialog.setMinimumSize(QSize(576, 320))
        Dialog.setMaximumSize(QSize(576, 320))
        Dialog.setBaseSize(QSize(576, 320))
        Dialog.setModal(True)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelExtractFilesMatchingFileMask = QLabel(Dialog)
        self.labelExtractFilesMatchingFileMask.setObjectName(u"labelExtractFilesMatchingFileMask")

        self.gridLayout.addWidget(self.labelExtractFilesMatchingFileMask, 0, 0, 1, 1)

        self.comboBoxExtractFilesMatchingFileMask = QComboBox(Dialog)
        self.comboBoxExtractFilesMatchingFileMask.addItem("")
        self.comboBoxExtractFilesMatchingFileMask.setObjectName(u"comboBoxExtractFilesMatchingFileMask")
        self.comboBoxExtractFilesMatchingFileMask.setEditable(True)

        self.gridLayout.addWidget(self.comboBoxExtractFilesMatchingFileMask, 0, 1, 1, 1)

        self.labelEditToTheDirectory = QLabel(Dialog)
        self.labelEditToTheDirectory.setObjectName(u"labelEditToTheDirectory")

        self.gridLayout.addWidget(self.labelEditToTheDirectory, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEditToTheDirectory = QLineEdit(Dialog)
        self.lineEditToTheDirectory.setObjectName(u"lineEditToTheDirectory")

        self.horizontalLayout.addWidget(self.lineEditToTheDirectory)

        self.pushButtonOpenDirectory = QPushButton(Dialog)
        self.pushButtonOpenDirectory.setObjectName(u"pushButtonOpenDirectory")
        icon = QIcon()
        icon.addFile(u"../pyCommander/pixmaps/dctheme/16x16/actions/cm_switchignorelist.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonOpenDirectory.setIcon(icon)

        self.horizontalLayout.addWidget(self.pushButtonOpenDirectory)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        self.checkBoxUnpackEachArchiveToSeparateSubdir = QCheckBox(Dialog)
        self.checkBoxUnpackEachArchiveToSeparateSubdir.setObjectName(u"checkBoxUnpackEachArchiveToSeparateSubdir")

        self.gridLayout.addWidget(self.checkBoxUnpackEachArchiveToSeparateSubdir, 2, 0, 1, 2)

        self.checkBoxUnpackPathNamesIfStoredWithFiles = QCheckBox(Dialog)
        self.checkBoxUnpackPathNamesIfStoredWithFiles.setObjectName(u"checkBoxUnpackPathNamesIfStoredWithFiles")
        self.checkBoxUnpackPathNamesIfStoredWithFiles.setChecked(True)

        self.gridLayout.addWidget(self.checkBoxUnpackPathNamesIfStoredWithFiles, 3, 0, 1, 2)

        self.checkBoxOverwriteExistingFiles = QCheckBox(Dialog)
        self.checkBoxOverwriteExistingFiles.setObjectName(u"checkBoxOverwriteExistingFiles")

        self.gridLayout.addWidget(self.checkBoxOverwriteExistingFiles, 4, 0, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelPassword = QLabel(Dialog)
        self.labelPassword.setObjectName(u"labelPassword")

        self.horizontalLayout_2.addWidget(self.labelPassword)

        self.lineEditPassword = QLineEdit(Dialog)
        self.lineEditPassword.setObjectName(u"lineEditPassword")

        self.horizontalLayout_2.addWidget(self.lineEditPassword)


        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Unpack files", None))
        self.labelExtractFilesMatchingFileMask.setText(QCoreApplication.translate("Dialog", u"Extract files matching file mask:", None))
        self.comboBoxExtractFilesMatchingFileMask.setItemText(0, QCoreApplication.translate("Dialog", u"*.*", None))

        self.labelEditToTheDirectory.setText(QCoreApplication.translate("Dialog", u"To the directory:", None))
        self.pushButtonOpenDirectory.setText("")
        self.checkBoxUnpackEachArchiveToSeparateSubdir.setText(QCoreApplication.translate("Dialog", u"Unpack each arcive to a separate subdir (name of the archive)", None))
        self.checkBoxUnpackPathNamesIfStoredWithFiles.setText(QCoreApplication.translate("Dialog", u"Unpack path names if stored with files", None))
        self.checkBoxOverwriteExistingFiles.setText(QCoreApplication.translate("Dialog", u"Overwrite existing files", None))
        self.labelPassword.setText(QCoreApplication.translate("Dialog", u"Password for encrypted files:", None))
    # retranslateUi

