# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_new_directory.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateNewDirectory(object):
    def setupUi(self, CreateNewDirectory):
        CreateNewDirectory.setObjectName("CreateNewDirectory")
        CreateNewDirectory.setWindowModality(QtCore.Qt.WindowModal)
        CreateNewDirectory.resize(512, 256)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CreateNewDirectory.sizePolicy().hasHeightForWidth())
        CreateNewDirectory.setSizePolicy(sizePolicy)
        CreateNewDirectory.setMinimumSize(QtCore.QSize(512, 254))
        CreateNewDirectory.setMaximumSize(QtCore.QSize(512, 256))
        CreateNewDirectory.setBaseSize(QtCore.QSize(512, 256))
        CreateNewDirectory.setSizeGripEnabled(False)
        CreateNewDirectory.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(CreateNewDirectory)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.labelInputNewDirectoryName = QtWidgets.QLabel(CreateNewDirectory)
        self.labelInputNewDirectoryName.setObjectName("labelInputNewDirectoryName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelInputNewDirectoryName)
        self.lineInputNewDirectoryName = QtWidgets.QLineEdit(CreateNewDirectory)
        self.lineInputNewDirectoryName.setObjectName("lineInputNewDirectoryName")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineInputNewDirectoryName)
        self.checkBoxExtendedSyntax = QtWidgets.QCheckBox(CreateNewDirectory)
        self.checkBoxExtendedSyntax.setObjectName("checkBoxExtendedSyntax")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.checkBoxExtendedSyntax)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(CreateNewDirectory)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.labelInputNewDirectoryName.setBuddy(self.lineInputNewDirectoryName)

        self.retranslateUi(CreateNewDirectory)
        self.buttonBox.accepted.connect(CreateNewDirectory.accept) # type: ignore
        self.buttonBox.rejected.connect(CreateNewDirectory.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(CreateNewDirectory)
        CreateNewDirectory.setTabOrder(self.lineInputNewDirectoryName, self.checkBoxExtendedSyntax)

    def retranslateUi(self, CreateNewDirectory):
        _translate = QtCore.QCoreApplication.translate
        CreateNewDirectory.setWindowTitle(_translate("CreateNewDirectory", "Create symbolic link"))
        self.labelInputNewDirectoryName.setText(_translate("CreateNewDirectory", "Input new directory name:"))
        self.checkBoxExtendedSyntax.setText(_translate("CreateNewDirectory", "Extended syntax"))
