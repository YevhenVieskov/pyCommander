# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_new_directorywSfnOM.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CreateNewDirectory(object):
    def setupUi(self, CreateNewDirectory):
        if not CreateNewDirectory.objectName():
            CreateNewDirectory.setObjectName(u"CreateNewDirectory")
        CreateNewDirectory.setWindowModality(Qt.WindowModal)
        CreateNewDirectory.resize(512, 256)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CreateNewDirectory.sizePolicy().hasHeightForWidth())
        CreateNewDirectory.setSizePolicy(sizePolicy)
        CreateNewDirectory.setMinimumSize(QSize(512, 254))
        CreateNewDirectory.setMaximumSize(QSize(512, 256))
        CreateNewDirectory.setBaseSize(QSize(512, 256))
        CreateNewDirectory.setSizeGripEnabled(False)
        CreateNewDirectory.setModal(True)
        self.verticalLayout = QVBoxLayout(CreateNewDirectory)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.labelInputNewDirectoryName = QLabel(CreateNewDirectory)
        self.labelInputNewDirectoryName.setObjectName(u"labelInputNewDirectoryName")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.labelInputNewDirectoryName)

        self.lineInputNewDirectoryName = QLineEdit(CreateNewDirectory)
        self.lineInputNewDirectoryName.setObjectName(u"lineInputNewDirectoryName")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineInputNewDirectoryName)

        self.checkBoxExtendedSyntax = QCheckBox(CreateNewDirectory)
        self.checkBoxExtendedSyntax.setObjectName(u"checkBoxExtendedSyntax")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.checkBoxExtendedSyntax)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(CreateNewDirectory)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.labelInputNewDirectoryName.setBuddy(self.lineInputNewDirectoryName)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.lineInputNewDirectoryName, self.checkBoxExtendedSyntax)

        self.retranslateUi(CreateNewDirectory)
        self.buttonBox.accepted.connect(CreateNewDirectory.accept)
        self.buttonBox.rejected.connect(CreateNewDirectory.reject)

        QMetaObject.connectSlotsByName(CreateNewDirectory)
    # setupUi

    def retranslateUi(self, CreateNewDirectory):
        CreateNewDirectory.setWindowTitle(QCoreApplication.translate("CreateNewDirectory", u"Create symbolic link", None))
        self.labelInputNewDirectoryName.setText(QCoreApplication.translate("CreateNewDirectory", u"Input new directory name:", None))
        self.checkBoxExtendedSyntax.setText(QCoreApplication.translate("CreateNewDirectory", u"Extended syntax", None))
    # retranslateUi

