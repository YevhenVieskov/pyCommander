# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'searchjbcLUB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1151, 681)
        self.actionNewSearch = QAction(MainWindow)
        self.actionNewSearch.setObjectName(u"actionNewSearch")
        self.actionNewSearchClearFilters = QAction(MainWindow)
        self.actionNewSearchClearFilters.setObjectName(u"actionNewSearchClearFilters")
        self.actionLastSearch = QAction(MainWindow)
        self.actionLastSearch.setObjectName(u"actionLastSearch")
        self.actionStart = QAction(MainWindow)
        self.actionStart.setObjectName(u"actionStart")
        self.actionCancel = QAction(MainWindow)
        self.actionCancel.setObjectName(u"actionCancel")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionCancelSearchAndCloseWindow = QAction(MainWindow)
        self.actionCancelSearchAndCloseWindow.setObjectName(u"actionCancelSearchAndCloseWindow")
        self.actionCancelSearchCloseAndFreeFromMemory = QAction(MainWindow)
        self.actionCancelSearchCloseAndFreeFromMemory.setObjectName(u"actionCancelSearchCloseAndFreeFromMemory")
        self.actionForAllOthersCancelCloseAndFreeFromMemory = QAction(MainWindow)
        self.actionForAllOthersCancelCloseAndFreeFromMemory.setObjectName(u"actionForAllOthersCancelCloseAndFreeFromMemory")
        self.actionForAllSearchesCancelCloseAndFreeMemory = QAction(MainWindow)
        self.actionForAllSearchesCancelCloseAndFreeMemory.setObjectName(u"actionForAllSearchesCancelCloseAndFreeMemory")
        self.actionGoToPageStandard = QAction(MainWindow)
        self.actionGoToPageStandard.setObjectName(u"actionGoToPageStandard")
        self.actionGoToPageAdvanced = QAction(MainWindow)
        self.actionGoToPageAdvanced.setObjectName(u"actionGoToPageAdvanced")
        self.actionGoToPagePlugins = QAction(MainWindow)
        self.actionGoToPagePlugins.setObjectName(u"actionGoToPagePlugins")
        self.actionGoToPageLoadSave = QAction(MainWindow)
        self.actionGoToPageLoadSave.setObjectName(u"actionGoToPageLoadSave")
        self.actionGoToPageResults = QAction(MainWindow)
        self.actionGoToPageResults.setObjectName(u"actionGoToPageResults")
        self.actionNewSearchInstance = QAction(MainWindow)
        self.actionNewSearchInstance.setObjectName(u"actionNewSearchInstance")
        self.actionViewCurrentSearchInstances = QAction(MainWindow)
        self.actionViewCurrentSearchInstances.setObjectName(u"actionViewCurrentSearchInstances")
        self.actionView = QAction(MainWindow)
        self.actionView.setObjectName(u"actionView")
        self.actionEdit = QAction(MainWindow)
        self.actionEdit.setObjectName(u"actionEdit")
        self.actionFeedToListbox = QAction(MainWindow)
        self.actionFeedToListbox.setObjectName(u"actionFeedToListbox")
        self.actionGoToFile = QAction(MainWindow)
        self.actionGoToFile.setObjectName(u"actionGoToFile")
        self.actionConfigurationOfSearches = QAction(MainWindow)
        self.actionConfigurationOfSearches.setObjectName(u"actionConfigurationOfSearches")
        self.actionConfigurationOfHotKeys = QAction(MainWindow)
        self.actionConfigurationOfHotKeys.setObjectName(u"actionConfigurationOfHotKeys")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.Standard = QWidget()
        self.Standard.setObjectName(u"Standard")
        self.gridLayout_4 = QGridLayout(self.Standard)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBoxDirectories = QGroupBox(self.Standard)
        self.groupBoxDirectories.setObjectName(u"groupBoxDirectories")
        self.verticalLayout_7 = QVBoxLayout(self.groupBoxDirectories)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayoutStartInDirectoryCheckBoxes = QHBoxLayout()
        self.horizontalLayoutStartInDirectoryCheckBoxes.setObjectName(u"horizontalLayoutStartInDirectoryCheckBoxes")
        self.labelStartInDirectory = QLabel(self.groupBoxDirectories)
        self.labelStartInDirectory.setObjectName(u"labelStartInDirectory")

        self.horizontalLayoutStartInDirectoryCheckBoxes.addWidget(self.labelStartInDirectory)

        self.horizontalSpacerStartInDirectory = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayoutStartInDirectoryCheckBoxes.addItem(self.horizontalSpacerStartInDirectory)

        self.checkBoxOpenedTabs = QCheckBox(self.groupBoxDirectories)
        self.checkBoxOpenedTabs.setObjectName(u"checkBoxOpenedTabs")

        self.horizontalLayoutStartInDirectoryCheckBoxes.addWidget(self.checkBoxOpenedTabs)

        self.checkBoxSelectedDirectoriesAndFiles = QCheckBox(self.groupBoxDirectories)
        self.checkBoxSelectedDirectoriesAndFiles.setObjectName(u"checkBoxSelectedDirectoriesAndFiles")

        self.horizontalLayoutStartInDirectoryCheckBoxes.addWidget(self.checkBoxSelectedDirectoriesAndFiles)

        self.checkBoxFollowSymlinks = QCheckBox(self.groupBoxDirectories)
        self.checkBoxFollowSymlinks.setObjectName(u"checkBoxFollowSymlinks")

        self.horizontalLayoutStartInDirectoryCheckBoxes.addWidget(self.checkBoxFollowSymlinks)


        self.verticalLayout_7.addLayout(self.horizontalLayoutStartInDirectoryCheckBoxes)

        self.horizontalLayoutStartInDirectoryPath = QHBoxLayout()
        self.horizontalLayoutStartInDirectoryPath.setObjectName(u"horizontalLayoutStartInDirectoryPath")
        self.lineEditStartInDirectory = QLineEdit(self.groupBoxDirectories)
        self.lineEditStartInDirectory.setObjectName(u"lineEditStartInDirectory")

        self.horizontalLayoutStartInDirectoryPath.addWidget(self.lineEditStartInDirectory)

        self.pushButtonFileOpen = QPushButton(self.groupBoxDirectories)
        self.pushButtonFileOpen.setObjectName(u"pushButtonFileOpen")

        self.horizontalLayoutStartInDirectoryPath.addWidget(self.pushButtonFileOpen)


        self.verticalLayout_7.addLayout(self.horizontalLayoutStartInDirectoryPath)

        self.horizontalLayoutExcludeSearchCheckBoxes = QHBoxLayout()
        self.horizontalLayoutExcludeSearchCheckBoxes.setObjectName(u"horizontalLayoutExcludeSearchCheckBoxes")
        self.labelExcludeSubdirectories = QLabel(self.groupBoxDirectories)
        self.labelExcludeSubdirectories.setObjectName(u"labelExcludeSubdirectories")

        self.horizontalLayoutExcludeSearchCheckBoxes.addWidget(self.labelExcludeSubdirectories)

        self.labelSearchSubdirectories = QLabel(self.groupBoxDirectories)
        self.labelSearchSubdirectories.setObjectName(u"labelSearchSubdirectories")

        self.horizontalLayoutExcludeSearchCheckBoxes.addWidget(self.labelSearchSubdirectories)


        self.verticalLayout_7.addLayout(self.horizontalLayoutExcludeSearchCheckBoxes)

        self.horizontalLayoutSearchSubdirCheckboxes = QHBoxLayout()
        self.horizontalLayoutSearchSubdirCheckboxes.setObjectName(u"horizontalLayoutSearchSubdirCheckboxes")
        self.comboBoxExcludeSubdirectories = QComboBox(self.groupBoxDirectories)
        self.comboBoxExcludeSubdirectories.setObjectName(u"comboBoxExcludeSubdirectories")
        self.comboBoxExcludeSubdirectories.setEditable(True)

        self.horizontalLayoutSearchSubdirCheckboxes.addWidget(self.comboBoxExcludeSubdirectories)

        self.comboBoxSearchSubdirectories = QComboBox(self.groupBoxDirectories)
        self.comboBoxSearchSubdirectories.addItem("")
        self.comboBoxSearchSubdirectories.addItem("")
        self.comboBoxSearchSubdirectories.addItem("")
        self.comboBoxSearchSubdirectories.addItem("")
        self.comboBoxSearchSubdirectories.addItem("")
        self.comboBoxSearchSubdirectories.addItem("")
        self.comboBoxSearchSubdirectories.addItem("")
        self.comboBoxSearchSubdirectories.addItem("")
        self.comboBoxSearchSubdirectories.addItem("")
        self.comboBoxSearchSubdirectories.addItem("")
        self.comboBoxSearchSubdirectories.addItem("")
        self.comboBoxSearchSubdirectories.addItem("")
        self.comboBoxSearchSubdirectories.addItem("")
        self.comboBoxSearchSubdirectories.addItem("")
        self.comboBoxSearchSubdirectories.addItem("")
        self.comboBoxSearchSubdirectories.addItem("")
        self.comboBoxSearchSubdirectories.addItem("")
        self.comboBoxSearchSubdirectories.addItem("")
        self.comboBoxSearchSubdirectories.addItem("")
        self.comboBoxSearchSubdirectories.addItem("")
        self.comboBoxSearchSubdirectories.addItem("")
        self.comboBoxSearchSubdirectories.addItem("")
        self.comboBoxSearchSubdirectories.addItem("")
        self.comboBoxSearchSubdirectories.addItem("")
        self.comboBoxSearchSubdirectories.addItem("")
        self.comboBoxSearchSubdirectories.addItem("")
        self.comboBoxSearchSubdirectories.addItem("")
        self.comboBoxSearchSubdirectories.addItem("")
        self.comboBoxSearchSubdirectories.addItem("")
        self.comboBoxSearchSubdirectories.addItem("")
        self.comboBoxSearchSubdirectories.addItem("")
        self.comboBoxSearchSubdirectories.addItem("")
        self.comboBoxSearchSubdirectories.setObjectName(u"comboBoxSearchSubdirectories")

        self.horizontalLayoutSearchSubdirCheckboxes.addWidget(self.comboBoxSearchSubdirectories)


        self.verticalLayout_7.addLayout(self.horizontalLayoutSearchSubdirCheckboxes)

        self.verticalSpacerDirectories = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacerDirectories)


        self.gridLayout_4.addWidget(self.groupBoxDirectories, 0, 0, 1, 1)

        self.horizontalSpacerDirectories = QSpacerItem(411, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacerDirectories, 0, 1, 1, 1)

        self.groupBoxFiles = QGroupBox(self.Standard)
        self.groupBoxFiles.setObjectName(u"groupBoxFiles")
        self.verticalLayout_5 = QVBoxLayout(self.groupBoxFiles)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayoutFileMask = QHBoxLayout()
        self.horizontalLayoutFileMask.setObjectName(u"horizontalLayoutFileMask")
        self.labelFileMask = QLabel(self.groupBoxFiles)
        self.labelFileMask.setObjectName(u"labelFileMask")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelFileMask.sizePolicy().hasHeightForWidth())
        self.labelFileMask.setSizePolicy(sizePolicy)
        self.labelFileMask.setBaseSize(QSize(64, 0))

        self.horizontalLayoutFileMask.addWidget(self.labelFileMask)

        self.horizontalSpacerFileMask = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayoutFileMask.addItem(self.horizontalSpacerFileMask)

        self.checkBoxSearchInArchives = QCheckBox(self.groupBoxFiles)
        self.checkBoxSearchInArchives.setObjectName(u"checkBoxSearchInArchives")

        self.horizontalLayoutFileMask.addWidget(self.checkBoxSearchInArchives)

        self.checkBoxSearchForPartOfFileName = QCheckBox(self.groupBoxFiles)
        self.checkBoxSearchForPartOfFileName.setObjectName(u"checkBoxSearchForPartOfFileName")

        self.horizontalLayoutFileMask.addWidget(self.checkBoxSearchForPartOfFileName)

        self.checkBoxRegularExpression = QCheckBox(self.groupBoxFiles)
        self.checkBoxRegularExpression.setObjectName(u"checkBoxRegularExpression")

        self.horizontalLayoutFileMask.addWidget(self.checkBoxRegularExpression)


        self.verticalLayout_5.addLayout(self.horizontalLayoutFileMask)

        self.lineEditFileMask = QLineEdit(self.groupBoxFiles)
        self.lineEditFileMask.setObjectName(u"lineEditFileMask")

        self.verticalLayout_5.addWidget(self.lineEditFileMask)

        self.labelExcludeFiles = QLabel(self.groupBoxFiles)
        self.labelExcludeFiles.setObjectName(u"labelExcludeFiles")

        self.verticalLayout_5.addWidget(self.labelExcludeFiles)

        self.comboBoxExcludeFiles = QComboBox(self.groupBoxFiles)
        self.comboBoxExcludeFiles.setObjectName(u"comboBoxExcludeFiles")
        self.comboBoxExcludeFiles.setEditable(True)

        self.verticalLayout_5.addWidget(self.comboBoxExcludeFiles)

        self.verticalSpacer = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.gridLayout_4.addWidget(self.groupBoxFiles, 1, 0, 1, 1)

        self.horizontalSpacerFiles = QSpacerItem(411, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacerFiles, 1, 1, 1, 1)

        self.groupBoxFindData = QGroupBox(self.Standard)
        self.groupBoxFindData.setObjectName(u"groupBoxFindData")
        self.verticalLayout_6 = QVBoxLayout(self.groupBoxFindData)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayoutFindTextInFile = QHBoxLayout()
        self.horizontalLayoutFindTextInFile.setObjectName(u"horizontalLayoutFindTextInFile")
        self.checkBoxFindTextInFile = QCheckBox(self.groupBoxFindData)
        self.checkBoxFindTextInFile.setObjectName(u"checkBoxFindTextInFile")

        self.horizontalLayoutFindTextInFile.addWidget(self.checkBoxFindTextInFile)

        self.lineEditFindTextInFile = QLineEdit(self.groupBoxFindData)
        self.lineEditFindTextInFile.setObjectName(u"lineEditFindTextInFile")

        self.horizontalLayoutFindTextInFile.addWidget(self.lineEditFindTextInFile)


        self.verticalLayout_6.addLayout(self.horizontalLayoutFindTextInFile)

        self.horizontalLayoutReplaceBy = QHBoxLayout()
        self.horizontalLayoutReplaceBy.setObjectName(u"horizontalLayoutReplaceBy")
        self.checkBoxReplaceBy = QCheckBox(self.groupBoxFindData)
        self.checkBoxReplaceBy.setObjectName(u"checkBoxReplaceBy")

        self.horizontalLayoutReplaceBy.addWidget(self.checkBoxReplaceBy)

        self.lineEditReplaceBy = QLineEdit(self.groupBoxFindData)
        self.lineEditReplaceBy.setObjectName(u"lineEditReplaceBy")

        self.horizontalLayoutReplaceBy.addWidget(self.lineEditReplaceBy)


        self.verticalLayout_6.addLayout(self.horizontalLayoutReplaceBy)

        self.gridLayoutFindDataCheckBoxes = QGridLayout()
        self.gridLayoutFindDataCheckBoxes.setObjectName(u"gridLayoutFindDataCheckBoxes")
        self.checkBoxFindFilesNotContainingText = QCheckBox(self.groupBoxFindData)
        self.checkBoxFindFilesNotContainingText.setObjectName(u"checkBoxFindFilesNotContainingText")

        self.gridLayoutFindDataCheckBoxes.addWidget(self.checkBoxFindFilesNotContainingText, 0, 0, 1, 2)

        self.checkBoxCaseSensitive = QCheckBox(self.groupBoxFindData)
        self.checkBoxCaseSensitive.setObjectName(u"checkBoxCaseSensitive")

        self.gridLayoutFindDataCheckBoxes.addWidget(self.checkBoxCaseSensitive, 0, 2, 1, 1)

        self.checkBoxRegularExpressionFindData = QCheckBox(self.groupBoxFindData)
        self.checkBoxRegularExpressionFindData.setObjectName(u"checkBoxRegularExpressionFindData")

        self.gridLayoutFindDataCheckBoxes.addWidget(self.checkBoxRegularExpressionFindData, 0, 3, 1, 1)

        self.checkBoxOfficeXML = QCheckBox(self.groupBoxFindData)
        self.checkBoxOfficeXML.setObjectName(u"checkBoxOfficeXML")

        self.gridLayoutFindDataCheckBoxes.addWidget(self.checkBoxOfficeXML, 0, 4, 1, 1)

        self.labelEncoding = QLabel(self.groupBoxFindData)
        self.labelEncoding.setObjectName(u"labelEncoding")

        self.gridLayoutFindDataCheckBoxes.addWidget(self.labelEncoding, 1, 0, 1, 1)

        self.comboBoxEncoding = QComboBox(self.groupBoxFindData)
        self.comboBoxEncoding.addItem("")
        self.comboBoxEncoding.addItem("")
        self.comboBoxEncoding.addItem("")
        self.comboBoxEncoding.addItem("")
        self.comboBoxEncoding.addItem("")
        self.comboBoxEncoding.addItem("")
        self.comboBoxEncoding.addItem("")
        self.comboBoxEncoding.addItem("")
        self.comboBoxEncoding.addItem("")
        self.comboBoxEncoding.addItem("")
        self.comboBoxEncoding.addItem("")
        self.comboBoxEncoding.addItem("")
        self.comboBoxEncoding.addItem("")
        self.comboBoxEncoding.addItem("")
        self.comboBoxEncoding.addItem("")
        self.comboBoxEncoding.addItem("")
        self.comboBoxEncoding.addItem("")
        self.comboBoxEncoding.addItem("")
        self.comboBoxEncoding.addItem("")
        self.comboBoxEncoding.addItem("")
        self.comboBoxEncoding.addItem("")
        self.comboBoxEncoding.addItem("")
        self.comboBoxEncoding.addItem("")
        self.comboBoxEncoding.addItem("")
        self.comboBoxEncoding.addItem("")
        self.comboBoxEncoding.addItem("")
        self.comboBoxEncoding.addItem("")
        self.comboBoxEncoding.addItem("")
        self.comboBoxEncoding.addItem("")
        self.comboBoxEncoding.addItem("")
        self.comboBoxEncoding.setObjectName(u"comboBoxEncoding")

        self.gridLayoutFindDataCheckBoxes.addWidget(self.comboBoxEncoding, 1, 1, 1, 1)

        self.checkBoxHexadecimal = QCheckBox(self.groupBoxFindData)
        self.checkBoxHexadecimal.setObjectName(u"checkBoxHexadecimal")

        self.gridLayoutFindDataCheckBoxes.addWidget(self.checkBoxHexadecimal, 1, 3, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayoutFindDataCheckBoxes)

        self.verticalSpacerFindData = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacerFindData)


        self.gridLayout_4.addWidget(self.groupBoxFindData, 2, 0, 1, 1)

        self.horizontalSpacerFindData = QSpacerItem(411, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacerFindData, 2, 1, 1, 1)

        self.verticalSpacerStandardTab = QSpacerItem(20, 122, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacerStandardTab, 3, 0, 1, 1)

        self.tabWidget.addTab(self.Standard, "")
        self.Advanced = QWidget()
        self.Advanced.setObjectName(u"Advanced")
        self.gridLayout_6 = QGridLayout(self.Advanced)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayoutDate = QGridLayout()
        self.gridLayoutDate.setObjectName(u"gridLayoutDate")
        self.checkBoxNotOlderThan = QCheckBox(self.Advanced)
        self.checkBoxNotOlderThan.setObjectName(u"checkBoxNotOlderThan")

        self.gridLayoutDate.addWidget(self.checkBoxNotOlderThan, 0, 0, 1, 1)

        self.spinBoxNotOlderThan = QSpinBox(self.Advanced)
        self.spinBoxNotOlderThan.setObjectName(u"spinBoxNotOlderThan")

        self.gridLayoutDate.addWidget(self.spinBoxNotOlderThan, 1, 0, 1, 1)

        self.comboBoxNotOlderThan = QComboBox(self.Advanced)
        self.comboBoxNotOlderThan.addItem("")
        self.comboBoxNotOlderThan.addItem("")
        self.comboBoxNotOlderThan.addItem("")
        self.comboBoxNotOlderThan.addItem("")
        self.comboBoxNotOlderThan.addItem("")
        self.comboBoxNotOlderThan.addItem("")
        self.comboBoxNotOlderThan.addItem("")
        self.comboBoxNotOlderThan.addItem("")
        self.comboBoxNotOlderThan.addItem("")
        self.comboBoxNotOlderThan.addItem("")
        self.comboBoxNotOlderThan.setObjectName(u"comboBoxNotOlderThan")

        self.gridLayoutDate.addWidget(self.comboBoxNotOlderThan, 1, 1, 1, 1)

        self.checkBoxSizeFrom = QCheckBox(self.Advanced)
        self.checkBoxSizeFrom.setObjectName(u"checkBoxSizeFrom")

        self.gridLayoutDate.addWidget(self.checkBoxSizeFrom, 2, 0, 1, 1)

        self.checkBoxSizeTo = QCheckBox(self.Advanced)
        self.checkBoxSizeTo.setObjectName(u"checkBoxSizeTo")

        self.gridLayoutDate.addWidget(self.checkBoxSizeTo, 2, 1, 1, 1)

        self.comboBoxSizeTo = QComboBox(self.Advanced)
        self.comboBoxSizeTo.addItem("")
        self.comboBoxSizeTo.addItem("")
        self.comboBoxSizeTo.addItem("")
        self.comboBoxSizeTo.addItem("")
        self.comboBoxSizeTo.addItem("")
        self.comboBoxSizeTo.setObjectName(u"comboBoxSizeTo")

        self.gridLayoutDate.addWidget(self.comboBoxSizeTo, 2, 2, 1, 1)

        self.checkBoxDateFrom = QCheckBox(self.Advanced)
        self.checkBoxDateFrom.setObjectName(u"checkBoxDateFrom")

        self.gridLayoutDate.addWidget(self.checkBoxDateFrom, 3, 0, 1, 1)

        self.checkBoxDateTo = QCheckBox(self.Advanced)
        self.checkBoxDateTo.setObjectName(u"checkBoxDateTo")

        self.gridLayoutDate.addWidget(self.checkBoxDateTo, 3, 1, 1, 1)

        self.checkBoxTimeFrom = QCheckBox(self.Advanced)
        self.checkBoxTimeFrom.setObjectName(u"checkBoxTimeFrom")

        self.gridLayoutDate.addWidget(self.checkBoxTimeFrom, 3, 2, 1, 1)

        self.checkBoxTimeTo = QCheckBox(self.Advanced)
        self.checkBoxTimeTo.setObjectName(u"checkBoxTimeTo")

        self.gridLayoutDate.addWidget(self.checkBoxTimeTo, 3, 3, 1, 1)

        self.dateEditFrom = QDateEdit(self.Advanced)
        self.dateEditFrom.setObjectName(u"dateEditFrom")

        self.gridLayoutDate.addWidget(self.dateEditFrom, 4, 0, 1, 1)

        self.dateEditDateTo = QDateEdit(self.Advanced)
        self.dateEditDateTo.setObjectName(u"dateEditDateTo")

        self.gridLayoutDate.addWidget(self.dateEditDateTo, 4, 1, 1, 1)

        self.timeEditTimeFrom = QTimeEdit(self.Advanced)
        self.timeEditTimeFrom.setObjectName(u"timeEditTimeFrom")

        self.gridLayoutDate.addWidget(self.timeEditTimeFrom, 4, 2, 1, 1)

        self.timeEditTimeTo = QTimeEdit(self.Advanced)
        self.timeEditTimeTo.setObjectName(u"timeEditTimeTo")

        self.gridLayoutDate.addWidget(self.timeEditTimeTo, 4, 3, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayoutDate, 0, 0, 1, 1)

        self.horizontalSpacerDate = QSpacerItem(604, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacerDate, 0, 1, 1, 1)

        self.lineDateAttribute = QFrame(self.Advanced)
        self.lineDateAttribute.setObjectName(u"lineDateAttribute")
        self.lineDateAttribute.setFrameShape(QFrame.HLine)
        self.lineDateAttribute.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.lineDateAttribute, 1, 0, 1, 1)

        self.horizontalSpacerHorizontalLine1 = QSpacerItem(604, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacerHorizontalLine1, 1, 1, 2, 1)

        self.horizontalLayoutAttributes = QHBoxLayout()
        self.horizontalLayoutAttributes.setObjectName(u"horizontalLayoutAttributes")
        self.labelAttribute = QLabel(self.Advanced)
        self.labelAttribute.setObjectName(u"labelAttribute")

        self.horizontalLayoutAttributes.addWidget(self.labelAttribute)

        self.horizontalSpacerAttributesIntermal = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayoutAttributes.addItem(self.horizontalSpacerAttributesIntermal)


        self.gridLayout_6.addLayout(self.horizontalLayoutAttributes, 2, 0, 2, 1)

        self.horizontalSpacerAttributes = QSpacerItem(604, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacerAttributes, 3, 1, 2, 1)

        self.horizontalLayoutAttributesButtons = QHBoxLayout()
        self.horizontalLayoutAttributesButtons.setObjectName(u"horizontalLayoutAttributesButtons")
        self.lineEditAttributes = QLineEdit(self.Advanced)
        self.lineEditAttributes.setObjectName(u"lineEditAttributes")

        self.horizontalLayoutAttributesButtons.addWidget(self.lineEditAttributes)

        self.pushButtonAdd = QPushButton(self.Advanced)
        self.pushButtonAdd.setObjectName(u"pushButtonAdd")

        self.horizontalLayoutAttributesButtons.addWidget(self.pushButtonAdd)

        self.pushButtonHelp = QPushButton(self.Advanced)
        self.pushButtonHelp.setObjectName(u"pushButtonHelp")

        self.horizontalLayoutAttributesButtons.addWidget(self.pushButtonHelp)


        self.gridLayout_6.addLayout(self.horizontalLayoutAttributesButtons, 4, 0, 2, 1)

        self.horizontalSpacerAttributesButton = QSpacerItem(604, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacerAttributesButton, 5, 1, 1, 1)

        self.horizontalSpacerHorisontalLine2 = QSpacerItem(604, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacerHorisontalLine2, 6, 1, 2, 1)

        self.lineAttributesFind = QFrame(self.Advanced)
        self.lineAttributesFind.setObjectName(u"lineAttributesFind")
        self.lineAttributesFind.setFrameShape(QFrame.HLine)
        self.lineAttributesFind.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.lineAttributesFind, 7, 0, 1, 1)

        self.horizontalLayoutFindDuplicateFiles = QHBoxLayout()
        self.horizontalLayoutFindDuplicateFiles.setObjectName(u"horizontalLayoutFindDuplicateFiles")
        self.checkBoxFindDuplicateFiles = QCheckBox(self.Advanced)
        self.checkBoxFindDuplicateFiles.setObjectName(u"checkBoxFindDuplicateFiles")

        self.horizontalLayoutFindDuplicateFiles.addWidget(self.checkBoxFindDuplicateFiles)

        self.horizontalSpacerFindDuplicateFilesInternal = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayoutFindDuplicateFiles.addItem(self.horizontalSpacerFindDuplicateFilesInternal)


        self.gridLayout_6.addLayout(self.horizontalLayoutFindDuplicateFiles, 8, 0, 1, 1)

        self.horizontalSpacerFindDuplicateFiles = QSpacerItem(604, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacerFindDuplicateFiles, 8, 1, 1, 1)

        self.horizontalLayoutCheckBoxes = QHBoxLayout()
        self.horizontalLayoutCheckBoxes.setObjectName(u"horizontalLayoutCheckBoxes")
        self.checkBoxSameName = QCheckBox(self.Advanced)
        self.checkBoxSameName.setObjectName(u"checkBoxSameName")

        self.horizontalLayoutCheckBoxes.addWidget(self.checkBoxSameName)

        self.checkBoxSameSize = QCheckBox(self.Advanced)
        self.checkBoxSameSize.setObjectName(u"checkBoxSameSize")

        self.horizontalLayoutCheckBoxes.addWidget(self.checkBoxSameSize)

        self.checkBoxSameHash = QCheckBox(self.Advanced)
        self.checkBoxSameHash.setObjectName(u"checkBoxSameHash")

        self.horizontalLayoutCheckBoxes.addWidget(self.checkBoxSameHash)

        self.checkBoxSomeContent = QCheckBox(self.Advanced)
        self.checkBoxSomeContent.setObjectName(u"checkBoxSomeContent")

        self.horizontalLayoutCheckBoxes.addWidget(self.checkBoxSomeContent)


        self.gridLayout_6.addLayout(self.horizontalLayoutCheckBoxes, 9, 0, 1, 1)

        self.horizontalSpacerCheckBoxesDuplicateFiles = QSpacerItem(604, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacerCheckBoxesDuplicateFiles, 9, 1, 1, 1)

        self.verticalSpacerAdvancedTab = QSpacerItem(20, 351, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacerAdvancedTab, 10, 0, 1, 1)

        self.tabWidget.addTab(self.Advanced, "")
        self.Plugins = QWidget()
        self.Plugins.setObjectName(u"Plugins")
        self.verticalLayout_4 = QVBoxLayout(self.Plugins)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayoutUseSearchPlugin = QHBoxLayout()
        self.horizontalLayoutUseSearchPlugin.setObjectName(u"horizontalLayoutUseSearchPlugin")
        self.checkBoxUseSearchPlugin = QCheckBox(self.Plugins)
        self.checkBoxUseSearchPlugin.setObjectName(u"checkBoxUseSearchPlugin")

        self.horizontalLayoutUseSearchPlugin.addWidget(self.checkBoxUseSearchPlugin)

        self.comboBoxUseSearchPlugin = QComboBox(self.Plugins)
        self.comboBoxUseSearchPlugin.setObjectName(u"comboBoxUseSearchPlugin")

        self.horizontalLayoutUseSearchPlugin.addWidget(self.comboBoxUseSearchPlugin)


        self.verticalLayout_4.addLayout(self.horizontalLayoutUseSearchPlugin)

        self.horizontalLayoutUseContentPlugin = QHBoxLayout()
        self.horizontalLayoutUseContentPlugin.setObjectName(u"horizontalLayoutUseContentPlugin")
        self.checkBoxUseContentPlugin = QCheckBox(self.Plugins)
        self.checkBoxUseContentPlugin.setObjectName(u"checkBoxUseContentPlugin")

        self.horizontalLayoutUseContentPlugin.addWidget(self.checkBoxUseContentPlugin)

        self.radioButtonAnd = QRadioButton(self.Plugins)
        self.radioButtonAnd.setObjectName(u"radioButtonAnd")

        self.horizontalLayoutUseContentPlugin.addWidget(self.radioButtonAnd)

        self.radioButtonOr = QRadioButton(self.Plugins)
        self.radioButtonOr.setObjectName(u"radioButtonOr")

        self.horizontalLayoutUseContentPlugin.addWidget(self.radioButtonOr)


        self.verticalLayout_4.addLayout(self.horizontalLayoutUseContentPlugin)

        self.tableWidgetPlugin = QTableWidget(self.Plugins)
        if (self.tableWidgetPlugin.columnCount() < 4):
            self.tableWidgetPlugin.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidgetPlugin.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidgetPlugin.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidgetPlugin.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidgetPlugin.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidgetPlugin.setObjectName(u"tableWidgetPlugin")

        self.verticalLayout_4.addWidget(self.tableWidgetPlugin)

        self.horizontalLayoutButtonsPluginTab = QHBoxLayout()
        self.horizontalLayoutButtonsPluginTab.setObjectName(u"horizontalLayoutButtonsPluginTab")
        self.horizontalSpacerButtons = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayoutButtonsPluginTab.addItem(self.horizontalSpacerButtons)

        self.pushButtonMoreRules = QPushButton(self.Plugins)
        self.pushButtonMoreRules.setObjectName(u"pushButtonMoreRules")

        self.horizontalLayoutButtonsPluginTab.addWidget(self.pushButtonMoreRules)

        self.pushButtonLessRules = QPushButton(self.Plugins)
        self.pushButtonLessRules.setObjectName(u"pushButtonLessRules")

        self.horizontalLayoutButtonsPluginTab.addWidget(self.pushButtonLessRules)


        self.verticalLayout_4.addLayout(self.horizontalLayoutButtonsPluginTab)

        self.tabWidget.addTab(self.Plugins, "")
        self.LoadSave = QWidget()
        self.LoadSave.setObjectName(u"LoadSave")
        self.verticalLayout_3 = QVBoxLayout(self.LoadSave)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayoutPreviousSearches = QGridLayout()
        self.gridLayoutPreviousSearches.setObjectName(u"gridLayoutPreviousSearches")
        self.labelPreviousSearches = QLabel(self.LoadSave)
        self.labelPreviousSearches.setObjectName(u"labelPreviousSearches")

        self.gridLayoutPreviousSearches.addWidget(self.labelPreviousSearches, 0, 0, 1, 1)

        self.textBrowserPrevious = QTextBrowser(self.LoadSave)
        self.textBrowserPrevious.setObjectName(u"textBrowserPrevious")

        self.gridLayoutPreviousSearches.addWidget(self.textBrowserPrevious, 1, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayoutPreviousSearches)

        self.horizontalLayoutButtonsLoadSaveTab = QHBoxLayout()
        self.horizontalLayoutButtonsLoadSaveTab.setObjectName(u"horizontalLayoutButtonsLoadSaveTab")
        self.horizontalSpacerLoadSaveTab = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayoutButtonsLoadSaveTab.addItem(self.horizontalSpacerLoadSaveTab)

        self.pushButtonLoad = QPushButton(self.LoadSave)
        self.pushButtonLoad.setObjectName(u"pushButtonLoad")

        self.horizontalLayoutButtonsLoadSaveTab.addWidget(self.pushButtonLoad)

        self.pushButtonSave = QPushButton(self.LoadSave)
        self.pushButtonSave.setObjectName(u"pushButtonSave")

        self.horizontalLayoutButtonsLoadSaveTab.addWidget(self.pushButtonSave)

        self.pushButtonSaveWithStartInDirectory = QPushButton(self.LoadSave)
        self.pushButtonSaveWithStartInDirectory.setObjectName(u"pushButtonSaveWithStartInDirectory")

        self.horizontalLayoutButtonsLoadSaveTab.addWidget(self.pushButtonSaveWithStartInDirectory)

        self.pushButtonDelete = QPushButton(self.LoadSave)
        self.pushButtonDelete.setObjectName(u"pushButtonDelete")

        self.horizontalLayoutButtonsLoadSaveTab.addWidget(self.pushButtonDelete)


        self.verticalLayout_3.addLayout(self.horizontalLayoutButtonsLoadSaveTab)

        self.tabWidget.addTab(self.LoadSave, "")
        self.Results = QWidget()
        self.Results.setObjectName(u"Results")
        self.verticalLayout_2 = QVBoxLayout(self.Results)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelScanning = QLabel(self.Results)
        self.labelScanning.setObjectName(u"labelScanning")

        self.gridLayout.addWidget(self.labelScanning, 0, 0, 1, 1)

        self.labelScannedTimeOfScan = QLabel(self.Results)
        self.labelScannedTimeOfScan.setObjectName(u"labelScannedTimeOfScan")

        self.gridLayout.addWidget(self.labelScannedTimeOfScan, 1, 0, 1, 1)

        self.labelFound = QLabel(self.Results)
        self.labelFound.setObjectName(u"labelFound")

        self.gridLayout.addWidget(self.labelFound, 1, 1, 1, 1)

        self.textBrowserResult = QTextBrowser(self.Results)
        self.textBrowserResult.setObjectName(u"textBrowserResult")

        self.gridLayout.addWidget(self.textBrowserResult, 2, 0, 1, 2)

        self.gridLayout.setColumnStretch(0, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.horizontalLayoutButtonsResultsTab = QHBoxLayout()
        self.horizontalLayoutButtonsResultsTab.setObjectName(u"horizontalLayoutButtonsResultsTab")
        self.horizontalSpacerResultsTab = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayoutButtonsResultsTab.addItem(self.horizontalSpacerResultsTab)

        self.pushButtonView = QPushButton(self.Results)
        self.pushButtonView.setObjectName(u"pushButtonView")

        self.horizontalLayoutButtonsResultsTab.addWidget(self.pushButtonView)

        self.pushButtonEdit = QPushButton(self.Results)
        self.pushButtonEdit.setObjectName(u"pushButtonEdit")

        self.horizontalLayoutButtonsResultsTab.addWidget(self.pushButtonEdit)

        self.pushButtonGoToFile = QPushButton(self.Results)
        self.pushButtonGoToFile.setObjectName(u"pushButtonGoToFile")

        self.horizontalLayoutButtonsResultsTab.addWidget(self.pushButtonGoToFile)

        self.pushButtonFeedToListbox = QPushButton(self.Results)
        self.pushButtonFeedToListbox.setObjectName(u"pushButtonFeedToListbox")

        self.horizontalLayoutButtonsResultsTab.addWidget(self.pushButtonFeedToListbox)


        self.verticalLayout_2.addLayout(self.horizontalLayoutButtonsResultsTab)

        self.tabWidget.addTab(self.Results, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        self.verticalLayoutButtonsContainer = QVBoxLayout()
        self.verticalLayoutButtonsContainer.setObjectName(u"verticalLayoutButtonsContainer")
        self.verticalLayoutButtons = QVBoxLayout()
        self.verticalLayoutButtons.setObjectName(u"verticalLayoutButtons")
        self.pushButtonStart = QPushButton(self.centralwidget)
        self.pushButtonStart.setObjectName(u"pushButtonStart")

        self.verticalLayoutButtons.addWidget(self.pushButtonStart)

        self.pushButtonCancel = QPushButton(self.centralwidget)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")

        self.verticalLayoutButtons.addWidget(self.pushButtonCancel)

        self.pushButtonClose = QPushButton(self.centralwidget)
        self.pushButtonClose.setObjectName(u"pushButtonClose")

        self.verticalLayoutButtons.addWidget(self.pushButtonClose)

        self.verticalSpacerBetweenButtons = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayoutButtons.addItem(self.verticalSpacerBetweenButtons)

        self.pushButtonNewSearch = QPushButton(self.centralwidget)
        self.pushButtonNewSearch.setObjectName(u"pushButtonNewSearch")

        self.verticalLayoutButtons.addWidget(self.pushButtonNewSearch)

        self.pushButtonLastSearch = QPushButton(self.centralwidget)
        self.pushButtonLastSearch.setObjectName(u"pushButtonLastSearch")

        self.verticalLayoutButtons.addWidget(self.pushButtonLastSearch)


        self.verticalLayoutButtonsContainer.addLayout(self.verticalLayoutButtons)

        self.verticalSpacerTopButtons = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayoutButtonsContainer.addItem(self.verticalSpacerTopButtons)


        self.horizontalLayout.addLayout(self.verticalLayoutButtonsContainer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1151, 26))
        self.menuAction = QMenu(self.menubar)
        self.menuAction.setObjectName(u"menuAction")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuResult = QMenu(self.menubar)
        self.menuResult.setObjectName(u"menuResult")
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.labelStartInDirectory.setBuddy(self.lineEditStartInDirectory)
        self.labelExcludeSubdirectories.setBuddy(self.comboBoxExcludeSubdirectories)
        self.labelSearchSubdirectories.setBuddy(self.comboBoxSearchSubdirectories)
        self.labelFileMask.setBuddy(self.lineEditFileMask)
        self.labelExcludeFiles.setBuddy(self.comboBoxExcludeFiles)
        self.labelEncoding.setBuddy(self.comboBoxEncoding)
        self.labelAttribute.setBuddy(self.lineEditAttributes)
#endif // QT_CONFIG(shortcut)

        self.menubar.addAction(self.menuAction.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuResult.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menuAction.addAction(self.actionNewSearch)
        self.menuAction.addAction(self.actionNewSearchClearFilters)
        self.menuAction.addAction(self.actionLastSearch)
        self.menuAction.addAction(self.actionStart)
        self.menuAction.addAction(self.actionCancel)
        self.menuAction.addSeparator()
        self.menuAction.addAction(self.actionClose)
        self.menuAction.addAction(self.actionCancelSearchAndCloseWindow)
        self.menuAction.addAction(self.actionCancelSearchCloseAndFreeFromMemory)
        self.menuAction.addAction(self.actionForAllOthersCancelCloseAndFreeFromMemory)
        self.menuAction.addAction(self.actionForAllSearchesCancelCloseAndFreeMemory)
        self.menuView.addAction(self.actionGoToPageStandard)
        self.menuView.addAction(self.actionGoToPageAdvanced)
        self.menuView.addAction(self.actionGoToPagePlugins)
        self.menuView.addAction(self.actionGoToPageLoadSave)
        self.menuView.addAction(self.actionGoToPageResults)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionNewSearchInstance)
        self.menuView.addAction(self.actionViewCurrentSearchInstances)
        self.menuResult.addAction(self.actionView)
        self.menuResult.addAction(self.actionEdit)
        self.menuResult.addAction(self.actionFeedToListbox)
        self.menuResult.addAction(self.actionGoToFile)
        self.menuOptions.addAction(self.actionConfigurationOfSearches)
        self.menuOptions.addAction(self.actionConfigurationOfHotKeys)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNewSearch.setText(QCoreApplication.translate("MainWindow", u"New search", None))
#if QT_CONFIG(shortcut)
        self.actionNewSearch.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionNewSearchClearFilters.setText(QCoreApplication.translate("MainWindow", u"New search (clear filters)", None))
#if QT_CONFIG(shortcut)
        self.actionNewSearchClearFilters.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionLastSearch.setText(QCoreApplication.translate("MainWindow", u"Last Search", None))
#if QT_CONFIG(shortcut)
        self.actionLastSearch.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
        self.actionStart.setText(QCoreApplication.translate("MainWindow", u"Start", None))
#if QT_CONFIG(shortcut)
        self.actionStart.setShortcut(QCoreApplication.translate("MainWindow", u"F9", None))
#endif // QT_CONFIG(shortcut)
        self.actionCancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionCancelSearchAndCloseWindow.setText(QCoreApplication.translate("MainWindow", u"Cancel search and close window", None))
#if QT_CONFIG(shortcut)
        self.actionCancelSearchAndCloseWindow.setShortcut(QCoreApplication.translate("MainWindow", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.actionCancelSearchCloseAndFreeFromMemory.setText(QCoreApplication.translate("MainWindow", u"Cancel search, close and free from memory", None))
#if QT_CONFIG(shortcut)
        self.actionCancelSearchCloseAndFreeFromMemory.setShortcut(QCoreApplication.translate("MainWindow", u"F4", None))
#endif // QT_CONFIG(shortcut)
        self.actionForAllOthersCancelCloseAndFreeFromMemory.setText(QCoreApplication.translate("MainWindow", u"For all others, cancel, close and free from memory", None))
        self.actionForAllSearchesCancelCloseAndFreeMemory.setText(QCoreApplication.translate("MainWindow", u"For all searches, cancel, close and free memory", None))
        self.actionGoToPageStandard.setText(QCoreApplication.translate("MainWindow", u"Go to page \"Standard\"", None))
#if QT_CONFIG(shortcut)
        self.actionGoToPageStandard.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+1", None))
#endif // QT_CONFIG(shortcut)
        self.actionGoToPageAdvanced.setText(QCoreApplication.translate("MainWindow", u"Go to page \"Advanced\"", None))
#if QT_CONFIG(shortcut)
        self.actionGoToPageAdvanced.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+2", None))
#endif // QT_CONFIG(shortcut)
        self.actionGoToPagePlugins.setText(QCoreApplication.translate("MainWindow", u"Go to page \"Plugins\"", None))
#if QT_CONFIG(shortcut)
        self.actionGoToPagePlugins.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+3", None))
#endif // QT_CONFIG(shortcut)
        self.actionGoToPageLoadSave.setText(QCoreApplication.translate("MainWindow", u"Go to page \"Load/Save\"", None))
#if QT_CONFIG(shortcut)
        self.actionGoToPageLoadSave.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+4", None))
#endif // QT_CONFIG(shortcut)
        self.actionGoToPageResults.setText(QCoreApplication.translate("MainWindow", u"Go to page \"Results\"", None))
#if QT_CONFIG(shortcut)
        self.actionGoToPageResults.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+5", None))
#endif // QT_CONFIG(shortcut)
        self.actionNewSearchInstance.setText(QCoreApplication.translate("MainWindow", u"New search instance...", None))
#if QT_CONFIG(shortcut)
        self.actionNewSearchInstance.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+F7", None))
#endif // QT_CONFIG(shortcut)
        self.actionViewCurrentSearchInstances.setText(QCoreApplication.translate("MainWindow", u"View current search instances", None))
        self.actionView.setText(QCoreApplication.translate("MainWindow", u"View", None))
#if QT_CONFIG(shortcut)
        self.actionView.setShortcut(QCoreApplication.translate("MainWindow", u"F3", None))
#endif // QT_CONFIG(shortcut)
        self.actionEdit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
#if QT_CONFIG(shortcut)
        self.actionEdit.setShortcut(QCoreApplication.translate("MainWindow", u"F4", None))
#endif // QT_CONFIG(shortcut)
        self.actionFeedToListbox.setText(QCoreApplication.translate("MainWindow", u"Feed to listbox", None))
        self.actionGoToFile.setText(QCoreApplication.translate("MainWindow", u"Go to file", None))
        self.actionConfigurationOfSearches.setText(QCoreApplication.translate("MainWindow", u"Configuration of searches", None))
        self.actionConfigurationOfHotKeys.setText(QCoreApplication.translate("MainWindow", u"Configuration of hot keys", None))
        self.groupBoxDirectories.setTitle(QCoreApplication.translate("MainWindow", u"Directories", None))
        self.labelStartInDirectory.setText(QCoreApplication.translate("MainWindow", u"Start in directory", None))
        self.checkBoxOpenedTabs.setText(QCoreApplication.translate("MainWindow", u"Opened tabs", None))
        self.checkBoxSelectedDirectoriesAndFiles.setText(QCoreApplication.translate("MainWindow", u"Selected directories and files", None))
        self.checkBoxFollowSymlinks.setText(QCoreApplication.translate("MainWindow", u"Follow symlinks", None))
        self.pushButtonFileOpen.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.labelExcludeSubdirectories.setText(QCoreApplication.translate("MainWindow", u"Exclude subdirectories", None))
        self.labelSearchSubdirectories.setText(QCoreApplication.translate("MainWindow", u"Search subdirectories", None))
        self.comboBoxExcludeSubdirectories.setCurrentText("")
        self.comboBoxSearchSubdirectories.setItemText(0, QCoreApplication.translate("MainWindow", u"all (unlimited depth)", None))
        self.comboBoxSearchSubdirectories.setItemText(1, QCoreApplication.translate("MainWindow", u"current dir only", None))
        self.comboBoxSearchSubdirectories.setItemText(2, QCoreApplication.translate("MainWindow", u"1 level(s)", None))
        self.comboBoxSearchSubdirectories.setItemText(3, QCoreApplication.translate("MainWindow", u"2 level(s)", None))
        self.comboBoxSearchSubdirectories.setItemText(4, QCoreApplication.translate("MainWindow", u"3 level(s)", None))
        self.comboBoxSearchSubdirectories.setItemText(5, QCoreApplication.translate("MainWindow", u"4 level(s)", None))
        self.comboBoxSearchSubdirectories.setItemText(6, QCoreApplication.translate("MainWindow", u"5 level(s)", None))
        self.comboBoxSearchSubdirectories.setItemText(7, QCoreApplication.translate("MainWindow", u"6 level(s)", None))
        self.comboBoxSearchSubdirectories.setItemText(8, QCoreApplication.translate("MainWindow", u"7 level(s)", None))
        self.comboBoxSearchSubdirectories.setItemText(9, QCoreApplication.translate("MainWindow", u"8 level(s)", None))
        self.comboBoxSearchSubdirectories.setItemText(10, QCoreApplication.translate("MainWindow", u"9 level(s)", None))
        self.comboBoxSearchSubdirectories.setItemText(11, QCoreApplication.translate("MainWindow", u"10 level(s)", None))
        self.comboBoxSearchSubdirectories.setItemText(12, QCoreApplication.translate("MainWindow", u"11 level(s)", None))
        self.comboBoxSearchSubdirectories.setItemText(13, QCoreApplication.translate("MainWindow", u"12 level(s)", None))
        self.comboBoxSearchSubdirectories.setItemText(14, QCoreApplication.translate("MainWindow", u"13 level(s)", None))
        self.comboBoxSearchSubdirectories.setItemText(15, QCoreApplication.translate("MainWindow", u"14 level(s)", None))
        self.comboBoxSearchSubdirectories.setItemText(16, QCoreApplication.translate("MainWindow", u"15 level(s)", None))
        self.comboBoxSearchSubdirectories.setItemText(17, QCoreApplication.translate("MainWindow", u"16 level(s)", None))
        self.comboBoxSearchSubdirectories.setItemText(18, QCoreApplication.translate("MainWindow", u"17 level(s)", None))
        self.comboBoxSearchSubdirectories.setItemText(19, QCoreApplication.translate("MainWindow", u"18 level(s)", None))
        self.comboBoxSearchSubdirectories.setItemText(20, QCoreApplication.translate("MainWindow", u"19 level(s)", None))
        self.comboBoxSearchSubdirectories.setItemText(21, QCoreApplication.translate("MainWindow", u"20 level(s)", None))
        self.comboBoxSearchSubdirectories.setItemText(22, QCoreApplication.translate("MainWindow", u"21 level(s)", None))
        self.comboBoxSearchSubdirectories.setItemText(23, QCoreApplication.translate("MainWindow", u"22 level(s)", None))
        self.comboBoxSearchSubdirectories.setItemText(24, QCoreApplication.translate("MainWindow", u"23 level(s)", None))
        self.comboBoxSearchSubdirectories.setItemText(25, QCoreApplication.translate("MainWindow", u"24 level(s)", None))
        self.comboBoxSearchSubdirectories.setItemText(26, QCoreApplication.translate("MainWindow", u"25 level(s)", None))
        self.comboBoxSearchSubdirectories.setItemText(27, QCoreApplication.translate("MainWindow", u"26 level(s)", None))
        self.comboBoxSearchSubdirectories.setItemText(28, QCoreApplication.translate("MainWindow", u"27 level(s)", None))
        self.comboBoxSearchSubdirectories.setItemText(29, QCoreApplication.translate("MainWindow", u"28 level(s)", None))
        self.comboBoxSearchSubdirectories.setItemText(30, QCoreApplication.translate("MainWindow", u"29 level(s)", None))
        self.comboBoxSearchSubdirectories.setItemText(31, QCoreApplication.translate("MainWindow", u"30 level(s)", None))

        self.groupBoxFiles.setTitle(QCoreApplication.translate("MainWindow", u"Files", None))
        self.labelFileMask.setText(QCoreApplication.translate("MainWindow", u"File mask", None))
        self.checkBoxSearchInArchives.setText(QCoreApplication.translate("MainWindow", u"Search in archives", None))
        self.checkBoxSearchForPartOfFileName.setText(QCoreApplication.translate("MainWindow", u"Search for part of file name", None))
        self.checkBoxRegularExpression.setText(QCoreApplication.translate("MainWindow", u"Regular expression", None))
        self.labelExcludeFiles.setText(QCoreApplication.translate("MainWindow", u"Exclude files", None))
        self.comboBoxExcludeFiles.setCurrentText("")
        self.groupBoxFindData.setTitle(QCoreApplication.translate("MainWindow", u"Find Data", None))
        self.checkBoxFindTextInFile.setText(QCoreApplication.translate("MainWindow", u"Find text in file", None))
        self.checkBoxReplaceBy.setText(QCoreApplication.translate("MainWindow", u"Replace by", None))
        self.checkBoxFindFilesNotContainingText.setText(QCoreApplication.translate("MainWindow", u"Find files NOT containing the text", None))
        self.checkBoxCaseSensitive.setText(QCoreApplication.translate("MainWindow", u"Case sensitive", None))
        self.checkBoxRegularExpressionFindData.setText(QCoreApplication.translate("MainWindow", u"Regular expression", None))
        self.checkBoxOfficeXML.setText(QCoreApplication.translate("MainWindow", u"Office XML", None))
        self.labelEncoding.setText(QCoreApplication.translate("MainWindow", u"Encoding:", None))
        self.comboBoxEncoding.setItemText(0, QCoreApplication.translate("MainWindow", u"Default", None))
        self.comboBoxEncoding.setItemText(1, QCoreApplication.translate("MainWindow", u"UTF-8", None))
        self.comboBoxEncoding.setItemText(2, QCoreApplication.translate("MainWindow", u"ANSI", None))
        self.comboBoxEncoding.setItemText(3, QCoreApplication.translate("MainWindow", u"OEM", None))
        self.comboBoxEncoding.setItemText(4, QCoreApplication.translate("MainWindow", u"cp1251", None))
        self.comboBoxEncoding.setItemText(5, QCoreApplication.translate("MainWindow", u"cp1252", None))
        self.comboBoxEncoding.setItemText(6, QCoreApplication.translate("MainWindow", u"cp1253", None))
        self.comboBoxEncoding.setItemText(7, QCoreApplication.translate("MainWindow", u"cp1254", None))
        self.comboBoxEncoding.setItemText(8, QCoreApplication.translate("MainWindow", u"cp1255", None))
        self.comboBoxEncoding.setItemText(9, QCoreApplication.translate("MainWindow", u"cp1256", None))
        self.comboBoxEncoding.setItemText(10, QCoreApplication.translate("MainWindow", u"cp1257", None))
        self.comboBoxEncoding.setItemText(11, QCoreApplication.translate("MainWindow", u"cp1258", None))
        self.comboBoxEncoding.setItemText(12, QCoreApplication.translate("MainWindow", u"cp437", None))
        self.comboBoxEncoding.setItemText(13, QCoreApplication.translate("MainWindow", u"cp850", None))
        self.comboBoxEncoding.setItemText(14, QCoreApplication.translate("MainWindow", u"cp852", None))
        self.comboBoxEncoding.setItemText(15, QCoreApplication.translate("MainWindow", u"cp866", None))
        self.comboBoxEncoding.setItemText(16, QCoreApplication.translate("MainWindow", u"cp874", None))
        self.comboBoxEncoding.setItemText(17, QCoreApplication.translate("MainWindow", u"cp932", None))
        self.comboBoxEncoding.setItemText(18, QCoreApplication.translate("MainWindow", u"cp936", None))
        self.comboBoxEncoding.setItemText(19, QCoreApplication.translate("MainWindow", u"cp949", None))
        self.comboBoxEncoding.setItemText(20, QCoreApplication.translate("MainWindow", u"cp950", None))
        self.comboBoxEncoding.setItemText(21, QCoreApplication.translate("MainWindow", u"ISO-8859-1", None))
        self.comboBoxEncoding.setItemText(22, QCoreApplication.translate("MainWindow", u"ISO-8859-2", None))
        self.comboBoxEncoding.setItemText(23, QCoreApplication.translate("MainWindow", u"ISO-8859-15", None))
        self.comboBoxEncoding.setItemText(24, QCoreApplication.translate("MainWindow", u"KOI8-R", None))
        self.comboBoxEncoding.setItemText(25, QCoreApplication.translate("MainWindow", u"KOI8-U", None))
        self.comboBoxEncoding.setItemText(26, QCoreApplication.translate("MainWindow", u"KOI8-RU", None))
        self.comboBoxEncoding.setItemText(27, QCoreApplication.translate("MainWindow", u"Macintosh", None))
        self.comboBoxEncoding.setItemText(28, QCoreApplication.translate("MainWindow", u"UTF-16LE", None))
        self.comboBoxEncoding.setItemText(29, QCoreApplication.translate("MainWindow", u"UTF-16BE", None))

        self.checkBoxHexadecimal.setText(QCoreApplication.translate("MainWindow", u"Hexadecimal", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Standard), QCoreApplication.translate("MainWindow", u"Standard", None))
        self.checkBoxNotOlderThan.setText(QCoreApplication.translate("MainWindow", u"Not older than:", None))
        self.comboBoxNotOlderThan.setItemText(0, QCoreApplication.translate("MainWindow", u"Second(s)", None))
        self.comboBoxNotOlderThan.setItemText(1, QCoreApplication.translate("MainWindow", u"Minute(s)", None))
        self.comboBoxNotOlderThan.setItemText(2, QCoreApplication.translate("MainWindow", u"Hour(s)", None))
        self.comboBoxNotOlderThan.setItemText(3, QCoreApplication.translate("MainWindow", u"Day(s)", None))
        self.comboBoxNotOlderThan.setItemText(4, QCoreApplication.translate("MainWindow", u"Week(s)", None))
        self.comboBoxNotOlderThan.setItemText(5, QCoreApplication.translate("MainWindow", u"Month(s)", None))
        self.comboBoxNotOlderThan.setItemText(6, QCoreApplication.translate("MainWindow", u"Year(s)", None))
        self.comboBoxNotOlderThan.setItemText(7, QCoreApplication.translate("MainWindow", u"Second(s)", None))
        self.comboBoxNotOlderThan.setItemText(8, QCoreApplication.translate("MainWindow", u"Second(s)", None))
        self.comboBoxNotOlderThan.setItemText(9, QCoreApplication.translate("MainWindow", u"Second(s)", None))

        self.checkBoxSizeFrom.setText(QCoreApplication.translate("MainWindow", u"Size from:", None))
        self.checkBoxSizeTo.setText(QCoreApplication.translate("MainWindow", u"Size to:", None))
        self.comboBoxSizeTo.setItemText(0, QCoreApplication.translate("MainWindow", u"Bytes", None))
        self.comboBoxSizeTo.setItemText(1, QCoreApplication.translate("MainWindow", u"Kilobytes", None))
        self.comboBoxSizeTo.setItemText(2, QCoreApplication.translate("MainWindow", u"Megabytes", None))
        self.comboBoxSizeTo.setItemText(3, QCoreApplication.translate("MainWindow", u"Gigabytes", None))
        self.comboBoxSizeTo.setItemText(4, QCoreApplication.translate("MainWindow", u"Terabytes", None))

        self.checkBoxDateFrom.setText(QCoreApplication.translate("MainWindow", u"Date from:", None))
        self.checkBoxDateTo.setText(QCoreApplication.translate("MainWindow", u"Date to:", None))
        self.checkBoxTimeFrom.setText(QCoreApplication.translate("MainWindow", u"Time from:", None))
        self.checkBoxTimeTo.setText(QCoreApplication.translate("MainWindow", u"Time to:", None))
        self.labelAttribute.setText(QCoreApplication.translate("MainWindow", u"Attributes", None))
        self.pushButtonAdd.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButtonHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.checkBoxFindDuplicateFiles.setText(QCoreApplication.translate("MainWindow", u"Find duplicate files:", None))
        self.checkBoxSameName.setText(QCoreApplication.translate("MainWindow", u"same name", None))
        self.checkBoxSameSize.setText(QCoreApplication.translate("MainWindow", u"same size", None))
        self.checkBoxSameHash.setText(QCoreApplication.translate("MainWindow", u"same hash", None))
        self.checkBoxSomeContent.setText(QCoreApplication.translate("MainWindow", u"some content", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Advanced), QCoreApplication.translate("MainWindow", u"Advanced", None))
        self.checkBoxUseSearchPlugin.setText(QCoreApplication.translate("MainWindow", u"Use search plugin:", None))
        self.checkBoxUseContentPlugin.setText(QCoreApplication.translate("MainWindow", u"Use content plugins, combine with:", None))
        self.radioButtonAnd.setText(QCoreApplication.translate("MainWindow", u"AND (all match)", None))
        self.radioButtonOr.setText(QCoreApplication.translate("MainWindow", u"OR (any match)", None))
        ___qtablewidgetitem = self.tableWidgetPlugin.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Plugin", None));
        ___qtablewidgetitem1 = self.tableWidgetPlugin.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Field", None));
        ___qtablewidgetitem2 = self.tableWidgetPlugin.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Operator", None));
        ___qtablewidgetitem3 = self.tableWidgetPlugin.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.pushButtonMoreRules.setText(QCoreApplication.translate("MainWindow", u"More rules", None))
        self.pushButtonLessRules.setText(QCoreApplication.translate("MainWindow", u"Less rules", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Plugins), QCoreApplication.translate("MainWindow", u"Plugins", None))
        self.labelPreviousSearches.setText(QCoreApplication.translate("MainWindow", u"Previous searches:", None))
        self.pushButtonLoad.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.pushButtonSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButtonSaveWithStartInDirectory.setText(QCoreApplication.translate("MainWindow", u"Save with \"Start in directory\"", None))
        self.pushButtonDelete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.LoadSave), QCoreApplication.translate("MainWindow", u"Load/Save", None))
        self.labelScanning.setText(QCoreApplication.translate("MainWindow", u"Scanning: Finished", None))
        self.labelScannedTimeOfScan.setText(QCoreApplication.translate("MainWindow", u"Scanned:550, Time of scan: 00:00:00.005", None))
        self.labelFound.setText(QCoreApplication.translate("MainWindow", u"Found:0", None))
        self.pushButtonView.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.pushButtonEdit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.pushButtonGoToFile.setText(QCoreApplication.translate("MainWindow", u"Go to file", None))
        self.pushButtonFeedToListbox.setText(QCoreApplication.translate("MainWindow", u"Feed to listbox", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Results), QCoreApplication.translate("MainWindow", u"Results", None))
        self.pushButtonStart.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButtonCancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.pushButtonClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.pushButtonNewSearch.setText(QCoreApplication.translate("MainWindow", u"New search", None))
        self.pushButtonLastSearch.setText(QCoreApplication.translate("MainWindow", u"Last search", None))
        self.menuAction.setTitle(QCoreApplication.translate("MainWindow", u"Action", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuResult.setTitle(QCoreApplication.translate("MainWindow", u"Result", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
    # retranslateUi

