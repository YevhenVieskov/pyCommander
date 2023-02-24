# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 22:17:21 2023

@author: Yevhen_Vieskov
"""
from pathlib import Path
import os
from PyQt5 import QtCore, QtGui, QtWidgets

w_resize = 1396
h_resize = 629

w_min = 640
w_max = 480

w_base = 800
h_base = 600


class DriveButton:
    def __init__(self, object_name = "", 
                 stretchFactorH = 0, stretchFactorV = 0, 
                 wmin = 48, hmin = 32, wmax = 48, hmax = 32, 
                 wbase = 48, hbase = 32, wicon = 16, hicon = 16,
                 path = "", icon_name = "drive-harddisk.png", 
                  flat = True,  parent = None):
        super().__init__(parent)
        self.object_name = object_name
        self.stretchFactorH = stretchFactorH
        self.stretchFactorV = stretchFactorV
        self.wmin = wmin
        self.hmin = hmin 
        self.wmax = wmax
        self.hmax = hmax 
        self.wbase = wbase
        self.hbase = hbase
        self.wicon = wicon
        self.hicon = hicon
        self.path = path
        self.icon_name = icon_name        
        self.flat = flat
        self.parent = parent #self.centralwidget
        self._initButton()
        
    def _initButton(self):
        self.pushButtonLeftDrive = QtWidgets.QPushButton(parent = self.parent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(self.stretchFactorH)
        sizePolicy.setVerticalStretch(self.stretchFactorV)
        sizePolicy.setHeightForWidth(self.pushButtonLeftDrive1.sizePolicy().hasHeightForWidth())
        self.pushButtonDrive.setSizePolicy(sizePolicy)
        self.pushButtonDrive.setMinimumSize(QtCore.QSize(self.wmin, self.hmin))
        self.pushButtonDrive.setMaximumSize(QtCore.QSize(self.wmax, self.hmax))
        self.pushButtonDrive.setBaseSize(QtCore.QSize(self.wbase, self.hbase))
        icon = QtGui.QIcon()
        full_path = os.path.join(self.path, self.icon_name)
        icon.addPixmap(QtGui.QPixmap(full_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonDrive.setIcon(icon)
        self.pushButtonDrive.setIconSize(QtCore.QSize(self.wicon, self.hicon))
        self.pushButtonDrive.setFlat(self.flat)
        self.pushButtonDrive.setObjectName(self.object_name)
        

class DrivesButtonBar:
    """Drives button bar"""
    def __init__(self, objectName = "horizontalLayoutButtonBar",
                 leftMargin = -1, topMargin = -1, 
                 rightMargin = -1, bottomMargin = 0, layoutSpacing = 7,
                 stretchFactorH = 0, stretchFactorV = 0,
                 wmin = 48, hmin = 32, wmax = 48, hmax = 32, 
                 wbase = 48,  hbase = 32,  wicon = 16,  hicon = 16,
                 wspacer = 40, hspacer = 20, path, parent):
        self.objectName = objectName
        self.leftMargin = leftMargin
        self.topMargin = topMargin
        self.rightMargin = rightMargin
        self.bottomMargin = bottomMargin
        self.layoutSpacing = layoutSpacing
        self.stretchFactorH = stretchFactorH
        self.stretchFactorV = stretchFactorV
        self.wmin = wmin
        self.hmin = hmin
        self.wmax = wmax
        self.hmax = hmax 
        self.wbase = wbase
        self.hbase = hbase
        self.wicon = wicon
        self.hicon = hicon
        self.wspacer = wspacer
        self.hspacer = hspacer
        self.path = ""
        self.parent = parent
        self.icons_list = ["camera-photo.png", "drive-harddisk.png", "drive-optical.png",
                           "drive-removable-media.png", "drive-removable-media-usb.png",
                           "drive-virtual.png", "media-flash.png", "media-floppy.png",
                           "media-optical.png", "network-wired.png"]
        self.drives_dict = {"C:\\" : "fixed"} 
        self.pushButtonDrive = []
        self._initDrivesButtonBar()


    def _initDrivesButtonBar(self):
        self.horizontalLayoutButtonBar = QtWidgets.QHBoxLayout()
        self.horizontalLayoutButtonBar.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayoutButtonBar.setContentsMargins(self.leftMargin, 
             self.topMargin, self.rightMargin, self.bottomMargin)
        self.horizontalLayoutButtonBar.setSpacing(self.layoutSpacing)
        self.horizontalLayoutButtonBar.setObjectName(self.objectName)
        n = len(self.drives_dict)
        n1 = n+1
        for i in range(n):
            iname = "drive-harddisk.png"
            if(i == n1):
                iname = "drive-virtual.png"  
            button = DrivesButtonBar( object_name = f"pushButtonDrive{i}",                          
                     path = self.path, icon_name = iname, 
                            parent = self.parent)
            self.pushButtonDrive.append(button)
            self.horizontalLayoutButtonBar.addWidget(button)        
        #VFS       
        spacerItem = QtWidgets.QSpacerItem(self.wspacer, self.hspacer, 
                QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutButtonBar.addItem(spacerItem)
        
       



class Window(QtWidgets.QMainWindow):
    """Main Window."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("pyCommander")
        self.resize(w_resize, h_resize)
        self.setMinimumSize(QtCore.QSize(w_min, w_max))
        self.setBaseSize(QtCore.QSize(w_base, h_base))
        self.setDocumentMode(False)
        self.centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setEnabled(True)
        self.centralWidget.setMouseTracking(True)
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setObjectName("gridLayout")   
        self._createActions()
        self._createMenuBar()
        self._createToolBars()
        
    def _createMenuBar(self):
        menubar = QtWidgets.QMenuBar()
        menubar.setGeometry(QtCore.QRect(0, 0, 1396, 26))
        menubar.setObjectName("menubar")
        
        menuFiles = QtWidgets.QMenu("&Files", menubar)
        menuFiles.setObjectName("menuFiles")
        menubar.addMenu(menuFiles)
        
        menuFiles.addAction(self.actionCreateSymbolicLink)
        menuFiles.addAction(self.actionCreateHardLink)
        menuFiles.addAction(self.actionCreateDirectory)
        menuFiles.addAction(self.actionCreateShortcut)
        menuFiles.addSeparator()
        menuFiles.addAction(self.actionChangeAttributes)
        menuFiles.addAction(self.actionShowFileProperties)
        menuFiles.addAction(self.actionEditComment)
        menuFiles.addAction(self.actionCalculateOccupiedSpace)
        menuFiles.addAction(self.actionCompareByContents)
        menuFiles.addAction(self.actionMultiRenameTool)
        menuFiles.addSeparator()
        menuFiles.addAction(self.actionPackFiles)
        menuFiles.addAction(self.actionExtractFiles)
        menuFiles.addAction(self.actionTestArchive)
        menuFiles.addAction(self.actionSplitFile)
        menuFiles.addAction(self.actionCombineFiles)
        menuFiles.addAction(self.actionCalculateChecksum)
        menuFiles.addAction(self.actionVerifyChecksum)
        menuFiles.addSeparator()
        menuFiles.addAction(self.actionWipe)
        menuFiles.addAction(self.actionDelete)
        menuFiles.addSeparator()
        menuFiles.addAction(self.actionExit)
        
        menuMark = QtWidgets.QMenu("&Mark", menubar)
        menuMark.setObjectName("menuMark")
        menubar.addMenu(menuMark)
        
        menuMark.addAction(self.actionSelectGroup)
        menuMark.addAction(self.actionUnselectGroup)
        menuMark.addAction(self.actionSelectAll)
        menuMark.addAction(self.actionUnselectAll)
        menuMark.addAction(self.actionInvertSelection)
        menuMark.addAction(self.actionSelectAllWithTheSameExtension)
        menuMark.addSeparator()
        menuMark.addAction(self.actionSaveSelection)
        menuMark.addAction(self.actionRestoreSelection)
        menuMark.addAction(self.actionSaveSelectionToFile)
        menuMark.addAction(self.actionLoadSelectionFromFile)
        menuMark.addAction(self.actionLoadSelectionFromClipboard)
        menuMark.addSeparator()
        menuMark.addAction(self.actionCopyFilenameToClipboard)
        menuMark.addAction(self.actionCopyFilenameWithFullPath)
        menuMark.addAction(self.actionCopyAllShownColumns)
        menuMark.addSeparator()
        menuMark.addAction(self.actionCompareDirectories)
        
        
        menuCommands = QtWidgets.QMenu("&Commands", menubar)
        menuCommands.setObjectName("menuCommands")
        menubar.addMenu(menuCommands)
        
        menuCommands.addAction(self.actionSearch)
        menuCommands.addAction(self.actionNewSearchInstance)
        menuCommands.addAction(self.actionViewCurrentSearchInstances)
        menuCommands.addAction(self.actionDirectoryHotlist)
        menuCommands.addAction(self.actionSynchronizeDirs)
        menuCommands.addSeparator()
        menuCommands.addAction(self.actionRunTerminal)
        menuCommands.addAction(self.actionExecuteInternalCommand)
        menuCommands.addSeparator()
        menuCommands.addAction(self.actionFlatView)
        menuCommands.addAction(self.actionOpenVFSList)
        menuCommands.addAction(self.actionSwapPanels)
        menuCommands.addAction(self.actionTargetSource)
        menuCommands.addSeparator()
        menuCommands.addAction(self.actionShowOccupiedSpace)
        
        
        menuNetwork = QtWidgets.QMenu("&Network", menubar)
        menuNetwork.setObjectName("menuNetwork")
        menubar.addMenu(menuNetwork)
        
        menuNetwork.addAction(self.actionNetworkConnect)
        menuNetwork.addAction(self.actionNetworkDisconnect)
        menuNetwork.addSeparator()
        menuNetwork.addAction(self.actionMapNetworkDrive)
        menuNetwork.addAction(self.actionDisconnectNetworkDrive)
        menuNetwork.addSeparator()
        menuNetwork.addAction(self.actionCopyNamesWithUNCPath)
                
        menuTabs = QtWidgets.QMenu("&Tabs", menubar)
        menuTabs.setObjectName("menuTabs")
        menubar.addMenu(menuTabs)
        
        menuTabs.addAction(self.actionNewTab)
        menuTabs.addAction(self.actionRenameTab)
        menuTabs.addAction(self.actionOpenFolderInNewTab)
        menuTabs.addSeparator()
        menuTabs.addAction(self.actionCloseTab)
        menuTabs.addAction(self.actionCloseTab)
        menuTabs.addAction(self.actionCloseDuplicateTabs)
        menuTabs.addSeparator()
        menuTabOption = menuTabs.addMenu("Tab Option")
        menuTabOption.addAction(self.actionNormal) 
        menuTabOption.addAction(self.actionLocked)
        menuTabOption.addAction(self.actionLockedWithDirectoryChangesAllowed)
        menuTabOption.addAction(self.actionLockedWithDirectoriesOpenedInNewTabs)
        menuTabOption.addSeparator()
        menuTabOption.addAction(self.actionSetAllTabsToNormal) 
        menuTabOption.addAction(self.actionSetAllTabsToLocked)
        menuTabOption.addAction(self.actionAllTabsLockedWithDirChangesAllowed)
        menuTabOption.addAction(self.actionAllTabsLockedWithDirOpenedInNewTabs)
       
        
        menuTabs.addSeparator()
        menuTabs.addAction(self.actionSwitchToNextTab)
        menuTabs.addAction(self.actionSwitchToPreviousTab)
        menuTabs.addSeparator()
        menuTabs.addAction(self.actionSaveTabsToFile)
        menuTabs.addAction(self.actionLoadTabsFromFile)
        menuTabs.addAction(self.actionSaveCurrentTabsToNewFavoriteTabs)
        menuTabs.addAction(self.actionLoadTabsFromFavoriteTabs)
        menuTabs.addSeparator()
        menuTabs.addAction(self.actionConfigurationOfFolderTabs)
        menuTabs.addAction(self.actionConfigurationOfFavoriteTabs)
       
        
        
        menuFavorities = QtWidgets.QMenu("&Favorities", menubar)
        menuFavorities.setObjectName("menuFavorities")
        menubar.addMenu(menuFavorities)
        
        menuFavorities.addAction(self.actionSaveCurrentTabsToNewFavoriteTabs)
        menuFavorities.addAction(self.actionResaveOnTheLastFavoriteTabsLoaded)
        menuFavorities.addAction(self.actionRelopadTheLastFavoriteTabsLoaded)
        menuFavorities.addAction(self.actionConfigurationOfFavoriteTabs)
        
        
        menuShow = QtWidgets.QMenu("&Show", menubar)
        menuShow.setObjectName("menuShow")
        menubar.addMenu(menuShow)
        
        menuShow.addAction(self.actionBriefView)
        menuShow.addAction(self.actionFull)
        menuShow.addAction(self.actionThumbnails)
        menuShow.addSeparator()
        menuShow.addAction(self.actionQuickViewPanel)
        menuShow.addAction(self.actionTreeViewPanel)
        menuShow.addSeparator()
        menuShow.addAction(self.actionSortByName)
        menuShow.addAction(self.actionSortByExtension)
        menuShow.addAction(self.actionSortBySize)
        menuShow.addAction(self.actionSortByDate)
        menuShow.addAction(self.actionSortByAttributes)
        menuShow.addSeparator()
        menuShow.addAction(self.actionReverseOrder)
        menuShow.addAction(self.actionRefresh)
        menuShow.addSeparator()
        menuShow.addAction(self.actionShowHiddenSystemFiles)
        menuShow.addSeparator()
        menuShow.addAction(self.actionHorizontalPanelsMode)
        menuShow.addSeparator()
        menuShow.addAction(self.actionOperationsViewer)
       
        
        
        menuConfiguration = QtWidgets.QMenu("&Configuration", menubar)
        menuConfiguration.setObjectName("menuConfiguration")
        menubar.addMenu(menuConfiguration)
        
        menuConfiguration.addAction(self.actionOptions)
        menuConfiguration.addSeparator()
        menuConfiguration.addAction(self.actionConfigurationOfDirectoryHotlist)
        menuConfiguration.addAction(self.actionConfigurationOfFileAssociations)
        menuConfiguration.addAction(self.actionConfigurationOfArchivers)
        menuConfiguration.addSeparator()
        menuConfiguration.addAction(self.actionSavePosition)
        menuConfiguration.addAction(self.actionSaveSettings)
             
        
        menuHelp = QtWidgets.QMenu("&Help", menubar)
        menuHelp.setObjectName("menuHelp")
        menubar.addMenu(menuHelp)  
        
        menuHelp.addAction(self.actionContents)
        menuHelp.addAction(self.actionKeyboard)
        menuHelp.addAction(self.actionVisitDoubleCommanderWebsite)
        menuHelp.addSeparator()
        menuHelp.addAction(self.actionAbout)
        
        self.setMenuBar(menubar)
        
        
      
    def _createToolBars(self):
        toolBar = QtWidgets.QToolBar()
        toolBar.setObjectName("toolBar")
        self.addToolBar(QtCore.Qt.TopToolBarArea, toolBar)
        
        
    def _createActions(self):    
        self.actionCreateSymbolicLink = QtWidgets.QAction(self)
        self.actionCreateSymbolicLink.setObjectName("actionCreateSymbolicLink")
        self.actionCreateSymbolicLink.setText("&Create Symbolic Link...")
        self.actionCreateSymbolicLink.setShortcut("")
        self.actionCreateSymbolicLink.setStatusTip("")
        
        self.actionCreateHardLink = QtWidgets.QAction(self)
        self.actionCreateHardLink.setObjectName("actionCreateHardLink")
        self.actionCreateHardLink.setText("&Create Hard Link...")
        self.actionCreateHardLink.setShortcut("")
        self.actionCreateHardLink.setStatusTip("")
        
        self.actionCreateDirectory = QtWidgets.QAction(self)
        self.actionCreateDirectory.setObjectName("actionCreateDirectory")
        self.actionCreateDirectory.setText("&Create Directory")
        self.actionCreateDirectory.setShortcut("")
        self.actionCreateDirectory.setStatusTip("F7")
        
        
        self.actionCreateShortcut = QtWidgets.QAction(self)
        self.actionCreateShortcut.setObjectName("actionCreateShortcut")
        self.actionCreateShortcut.setText("&Create Shortcut...")
        self.actionCreateShortcut.setShortcut("")
        self.actionCreateShortcut.setStatusTip("")
        
        self.actionChangeAttributes = QtWidgets.QAction(self)
        self.actionChangeAttributes.setObjectName("actionChangeAttributes")
        self.actionChangeAttributes.setText("&Change Attributes...")
        self.actionCreateShortcut.setShortcut("")
        self.actionCreateShortcut.setStatusTip("")
        
        self.actionShowFileProperties = QtWidgets.QAction(self)
        self.actionShowFileProperties.setObjectName("actionShowFileProperties")
        self.actionShowFileProperties.setText("&Show File Properties")
        self.actionShowFileProperties.setShortcut("Alt+Enter")
        self.actionShowFileProperties.setStatusTip("")
        
        self.actionEditComment = QtWidgets.QAction(self)
        self.actionEditComment.setObjectName("actionEditComment")
        self.actionEditComment.setText("&Edit Comment...")
        self.actionEditComment.setShortcut("")
        self.actionEditComment.setStatusTip("")
        
        self.actionCalculateOccupiedSpace = QtWidgets.QAction(self)
        self.actionCalculateOccupiedSpace.setObjectName("actionCalculateOccupiedSpace")
        self.actionCalculateOccupiedSpace.setText("&Calculate Occupied Space")
        self.actionCalculateOccupiedSpace.setShortcut("Ctrl+L")
        self.actionCalculateOccupiedSpace.setStatusTip("")
        
        self.actionCompareByContents = QtWidgets.QAction(self)
        self.actionCompareByContents.setObjectName("actionCompareByContents")
        self.actionCompareByContents.setText("&Compare By Contents")
        self.actionCompareByContents.setShortcut("")
        self.actionCompareByContents.setStatusTip("")
        
        self.actionMultiRenameTool = QtWidgets.QAction(self)
        self.actionMultiRenameTool.setObjectName("actionMultiRenameTool")
        self.actionMultiRenameTool.setText("&Multi Rename Tool")
        self.actionMultiRenameTool.setShortcut("Ctrl+M")
        self.actionMultiRenameTool.setStatusTip("")
        
        self.actionPackFiles = QtWidgets.QAction(self)
        self.actionPackFiles.setObjectName("actionPackFiles")
        self.actionPackFiles.setText("&Pack Files")
        self.actionPackFiles.setShortcut("")
        self.actionPackFiles.setStatusTip("Alt+F5")
        
        self.actionExtractFiles = QtWidgets.QAction(self)
        self.actionExtractFiles.setObjectName("actionExtractFiles")
        self.actionExtractFiles.setText("&Extract Files...")
        self.actionExtractFiles.setShortcut("")
        self.actionExtractFiles.setStatusTip("Alt+F9")
        
        
        self.actionTestArchive = QtWidgets.QAction(self)
        self.actionTestArchive.setObjectName("actionTestArchive")
        self.actionTestArchive.setText("&Test Archive")
        self.actionTestArchive.setShortcut("")
        self.actionTestArchive.setStatusTip("Shift+Alt+F9")
        
        self.actionSplitFile = QtWidgets.QAction(self)
        self.actionSplitFile.setObjectName("actionSplitFile")
        self.actionSplitFile.setText("&Split File...")
        self.actionSplitFile.setShortcut("")
        self.actionSplitFile.setStatusTip("")
        
        self.actionCombineFiles = QtWidgets.QAction(self)
        self.actionCombineFiles.setObjectName("actionCombineFiles")
        self.actionCombineFiles.setText("&Combine Files...")
        self.actionCombineFiles.setShortcut("")
        self.actionCombineFiles.setStatusTip("")
        
        self.actionCalculateChecksum = QtWidgets.QAction(self)
        self.actionCalculateChecksum.setObjectName("actionCalculateChecksum")
        self.actionCalculateChecksum.setText("&Calculate Checksum...")
        self.actionCalculateChecksum.setShortcut("")
        self.actionCalculateChecksum.setStatusTip("")
        
        self.actionVerifyChecksum = QtWidgets.QAction(self)
        self.actionVerifyChecksum.setObjectName("actionVerifyChecksum")
        self.actionVerifyChecksum.setText("&Verify Checksum...")
        self.actionVerifyChecksum.setShortcut("")
        self.actionVerifyChecksum.setStatusTip("")
        
        self.actionWipe = QtWidgets.QAction(self)
        self.actionWipe.setObjectName("actionWipe")
        self.actionWipe.setText("&Wipe")
        self.actionWipe.setShortcut("Alt+Del")
        self.actionWipe.setStatusTip("")
        
        self.actionDelete = QtWidgets.QAction(self)
        self.actionDelete.setObjectName("actionDelete")
        self.actionDelete.setText("&Delete")
        self.actionDelete.setShortcut("F8")
        self.actionDelete.setStatusTip("")
        
        self.actionExit = QtWidgets.QAction(self)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.setText("&Exit")
        self.actionExit.setShortcut("Alt+X")
        self.actionExit.setStatusTip("")
        
        
        self.actionSelectGroup = QtWidgets.QAction(self)
        self.actionSelectGroup.setObjectName("actionSelectGroup")
        self.actionSelectGroup.setText("&Select Group...")
        self.actionSelectGroup.setShortcut("")
        self.actionSelectGroup.setStatusTip("")
        
        self.actionUnselectGroup = QtWidgets.QAction(self)
        self.actionUnselectGroup.setObjectName("actionUnselectGroup")
        self.actionUnselectGroup.setText("&Unselect Group...")
        self.actionUnselectGroup.setShortcut("")
        self.actionUnselectGroup.setStatusTip("")
        
        self.actionSelectAll = QtWidgets.QAction(self)
        self.actionSelectAll.setObjectName("actionSelectAll")
        self.actionSelectAll.setText("&Select All")
        self.actionSelectAll.setShortcut("")
        self.actionSelectAll.setStatusTip("")
        
        self.actionUnselectAll = QtWidgets.QAction(self)
        self.actionUnselectAll.setObjectName("actionUnselectAll")
        self.actionUnselectAll.setText("&Unselect All")
        self.actionUnselectAll.setShortcut("")
        self.actionUnselectAll.setStatusTip("")
        
        self.actionInvertSelection = QtWidgets.QAction(self)
        self.actionInvertSelection.setObjectName("actionInvertSelection")
        self.actionInvertSelection.setText("&Invert Selection")
        self.actionInvertSelection.setShortcut("")
        self.actionInvertSelection.setStatusTip("")
        
        self.actionSelectAllWithTheSameExtension = QtWidgets.QAction(self)       
        self.actionSelectAllWithTheSameExtension.setObjectName("actionSelectAllWithTheSameExtension")
        self.actionSelectAllWithTheSameExtension.setText("&Select All with the Same Extension")
        self.actionSelectAllWithTheSameExtension.setShortcut("")
        self.actionSelectAllWithTheSameExtension.setStatusTip("")
        
        
        '''self.actionUnselectAllWithTheSameExtension = QtWidgets.QAction(self)        
        self.actionUnselectAllWithTheSameExtension.setObjectName("actionUnselectAllWithTheSameExtension")
        self.actionCreateSymbolicLink.setText("&Unselect All with the same Extension")'''
        
        self.actionSaveSelection = QtWidgets.QAction(self)         
        self.actionSaveSelection.setObjectName("actionSaveSelection")
        self.actionSaveSelection.setText("&Save Selection")
        self.actionSaveSelection.setShortcut("")
        self.actionSaveSelection.setStatusTip("")
        
        self.actionRestoreSelection = QtWidgets.QAction(self)       
        self.actionRestoreSelection.setObjectName("actionRestoreSelection")
        self.actionRestoreSelection.setText("&Restore Selection")
        self.actionRestoreSelection.setShortcut("")
        self.actionRestoreSelection.setStatusTip("")
        
        self.actionSaveSelectionToFile = QtWidgets.QAction(self)
        self.actionSaveSelectionToFile.setObjectName("actionSaveSelectionToFile")
        self.actionSaveSelectionToFile.setText("&Save Selection To File...")
        self.actionSaveSelectionToFile.setShortcut("")
        self.actionSaveSelectionToFile.setStatusTip("")
        
        self.actionLoadSelectionFromFile = QtWidgets.QAction(self)
        self.actionLoadSelectionFromFile.setObjectName("actionLoadSelectionFromFile")
        self.actionLoadSelectionFromFile.setText("&Load Selection From File...")
        self.actionLoadSelectionFromFile.setShortcut("")
        self.actionLoadSelectionFromFile.setStatusTip("")
        
        self.actionLoadSelectionFromClipboard = QtWidgets.QAction(self)
        self.actionLoadSelectionFromClipboard.setObjectName("actionLoadSelectionFromClipboard")
        self.actionLoadSelectionFromClipboard.setText("&Load Selection From Clipboard")
        self.actionLoadSelectionFromClipboard.setShortcut("")
        self.actionLoadSelectionFromClipboard.setStatusTip("")
        
        self.actionCopyFilenameToClipboard = QtWidgets.QAction(self)
        self.actionCopyFilenameToClipboard.setObjectName("actionCopyFilenameToClipboard")
        self.actionCopyFilenameToClipboard.setText("&Copy Filename(s) To Clipboard")
        self.actionCopyFilenameToClipboard.setShortcut("")
        self.actionCopyFilenameToClipboard.setStatusTip("Shift+Ctrl+X")
        
        self.actionCopyFilenameWithFullPath = QtWidgets.QAction(self)
        self.actionCopyFilenameWithFullPath.setObjectName("actionCopyFilenameWithFullPath")
        self.actionCopyFilenameWithFullPath.setText("&Copy Filename(s) With Full Path")
        self.actionCopyFilenameWithFullPath.setShortcut("")
        self.actionCopyFilenameWithFullPath.setStatusTip("Shift+Ctrl+C")
        
        self.actionCopyAllShownColumns = QtWidgets.QAction(self)
        self.actionCopyAllShownColumns.setObjectName("actionCopyAllShownColumns")
        self.actionCopyAllShownColumns.setText("&Copy All Shown Columns")
        self.actionCopyAllShownColumns.setShortcut("")
        self.actionCopyAllShownColumns.setStatusTip("")
        
        self.actionCompareDirectories = QtWidgets.QAction(self)
        self.actionCompareDirectories.setObjectName("actionCompareDirectories")
        self.actionCompareDirectories.setText("&Compare Directories")
        self.actionCompareDirectories.setShortcut("")
        self.actionCompareDirectories.setStatusTip("")
        
        self.actionSearch = QtWidgets.QAction(self)
        self.actionSearch.setObjectName("actionSearch")
        self.actionSearch.setText("&Search...")
        self.actionSearch.setShortcut("")
        self.actionSearch.setStatusTip("Alt+F7")
        
        self.actionNewSearchInstance = QtWidgets.QAction(self)
        self.actionNewSearchInstance.setObjectName("actionNewSearchInstance")
        self.actionNewSearchInstance.setText("&New Search Instance...")
        self.actionNewSearchInstance.setShortcut("")
        self.actionNewSearchInstance.setStatusTip("Shift+Ctrl+F7")
        
        self.actionViewCurrentSearchInstances = QtWidgets.QAction(self)
        self.actionViewCurrentSearchInstances.setObjectName("actionViewCurrentSearchInstances")
        self.actionViewCurrentSearchInstances.setText("&View Current Search Instances")
        self.actionViewCurrentSearchInstances.setShortcut("")
        self.actionViewCurrentSearchInstances.setStatusTip("")
        
        self.actionDirectoryHotlist = QtWidgets.QAction(self)
        self.actionDirectoryHotlist.setObjectName("actionDirectoryHotlist")
        self.actionDirectoryHotlist.setText("&Directory Hotlist")
        self.actionDirectoryHotlist.setShortcut("")
        self.actionDirectoryHotlist.setStatusTip("")
        
        self.actionSynchronizeDirs = QtWidgets.QAction(self)
        self.actionSynchronizeDirs.setObjectName("actionSynchronizeDirs")
        self.actionSynchronizeDirs.setText("&Synchronize dirs...")
        self.actionSynchronizeDirs.setShortcut("")
        self.actionSynchronizeDirs.setStatusTip("")
        
        self.actionRunTerminal = QtWidgets.QAction(self)
        self.actionRunTerminal.setObjectName("actionRunTerminal")
        self.actionRunTerminal.setText("&Run Terminal")
        self.actionRunTerminal.setShortcut("")
        self.actionRunTerminal.setStatusTip("F9")
        
        self.actionExecuteInternalCommand = QtWidgets.QAction(self)
        self.actionExecuteInternalCommand.setObjectName("actionExecuteInternalCommand")
        self.actionExecuteInternalCommand.setText("&Execute internal command...")
        self.actionExecuteInternalCommand.setShortcut("")
        self.actionExecuteInternalCommand.setStatusTip("Shift+F12")
        
        self.actionFlatView = QtWidgets.QAction(self)
        self.actionFlatView.setObjectName("actionFlatView")
        self.actionFlatView.setText("&Flat View")
        self.actionFlatView.setShortcut("")
        self.actionFlatView.setStatusTip("Ctrl+B")
        
        self.actionOpenVFSList = QtWidgets.QAction(self)
        self.actionOpenVFSList.setObjectName("actionOpenVFSList")
        self.actionOpenVFSList.setText("&Open VFS List")
        self.actionOpenVFSList.setShortcut("")
        self.actionOpenVFSList.setStatusTip("")
        
        self.actionSwapPanels = QtWidgets.QAction(self)
        self.actionSwapPanels.setObjectName("actionSwapPanels")
        self.actionSwapPanels.setText("&Swap Panels")                
        self.actionSwapPanels.setShortcut("Ctrl+U")
        self.actionSwapPanels.setStatusTip("")
        
        self.actionTargetSource = QtWidgets.QAction(self)
        self.actionTargetSource.setObjectName("actionTargetSource")
        self.actionTargetSource.setText("&Target Source")
        self.actionTargetSource.setShortcut("Alt+Z")
        self.actionTargetSource.setStatusTip("")
        
        self.actionShowOccupiedSpace = QtWidgets.QAction(self)
        self.actionShowOccupiedSpace.setObjectName("actionShowOccupiedSpace")
        self.actionShowOccupiedSpace.setText("&Show Occupied Space")
        self.actionShowOccupiedSpace.setShortcut("Shift+Alt+Enter")
        self.actionShowOccupiedSpace.setStatusTip("")
        
        self.actionNetworkConnect = QtWidgets.QAction(self)
        self.actionNetworkConnect.setObjectName("actionNetworkConnect")
        self.actionNetworkConnect.setText("&Network Connect...")
        self.actionNetworkConnect.setShortcut("")
        self.actionNetworkConnect.setStatusTip("")
        
        self.actionNetworkDisconnect  = QtWidgets.QAction(self)
        self.actionNetworkDisconnect.setObjectName("actionNetworkDisconnect")
        self.actionNetworkDisconnect.setText("&Network Disconnect")
        self.actionNetworkDisconnect.setShortcut("")
        self.actionNetworkDisconnect.setStatusTip("")
        
        self.actionMapNetworkDrive = QtWidgets.QAction(self)
        self.actionMapNetworkDrive.setObjectName("actionMapNetworkDrive")
        self.actionMapNetworkDrive.setText("&Map Network Drive...")
        self.actionMapNetworkDrive.setShortcut("")
        self.actionMapNetworkDrive.setStatusTip("")
        
        self.actionDisconnectNetworkDrive = QtWidgets.QAction(self)
        self.actionDisconnectNetworkDrive.setObjectName("actionDisconnectNetworkDrive")
        self.actionDisconnectNetworkDrive.setText("&Disconnect Network Drive...")
        self.actionDisconnectNetworkDrive.setShortcut("")
        self.actionDisconnectNetworkDrive.setStatusTip("")
        
        self.actionCopyNamesWithUNCPath = QtWidgets.QAction(self)
        self.actionCopyNamesWithUNCPath.setObjectName("actionCopyNamesWithUNCPath")
        self.actionCopyNamesWithUNCPath.setText("&Copy Names With UNC Path")
        self.actionCopyNamesWithUNCPath.setShortcut("")
        self.actionCopyNamesWithUNCPath.setStatusTip("")
        
        self.actionNewTab = QtWidgets.QAction(self)
        self.actionNewTab.setObjectName("actionNewTab")
        self.actionNewTab.setText("&New Tab")
        self.actionNewTab.setShortcut("Ctrl+T")
        self.actionNewTab.setStatusTip("")
        
        self.actionRenameTab = QtWidgets.QAction(self)
        self.actionRenameTab.setObjectName("actionRenameTab")
        self.actionRenameTab.setText("&Rename Tab")
        self.actionRenameTab.setShortcut("")
        self.actionRenameTab.setStatusTip("")
        
        self.actionOpenFolderInNewTab = QtWidgets.QAction(self)
        self.actionOpenFolderInNewTab.setObjectName("actionOpenFolderInNewTab")
        self.actionOpenFolderInNewTab.setText("&Open Folder In New Tab")
        self.actionOpenFolderInNewTab.setShortcut("Ctrl+Up")
        self.actionOpenFolderInNewTab.setStatusTip("")
        
        self.actionCloseTab = QtWidgets.QAction(self)
        self.actionCloseTab.setObjectName("actionCloseTab")
        self.actionCloseTab.setText("&Close Tab")
        self.actionCloseTab.setShortcut("Ctrl+W")
        self.actionCloseTab.setStatusTip("")
        
        '''self.actionCloseAllTabs = QtWidgets.QAction(self)
        self.actionCloseAllTabs.setObjectName("actionCloseAllTabs")
        self.actionCloseAllTabs.setText("&Close All Tabs")
        self.actionCloseAllTabs.setShortcut("")
        self.actionCloseAllTabs.setStatusTip("")'''
        
        self.actionCloseDuplicateTabs = QtWidgets.QAction(self)
        self.actionCloseDuplicateTabs.setObjectName("actionCloseDuplicateTabs")
        self.actionCloseDuplicateTabs.setText("&Close Duplicate Tabs")
        self.actionCloseDuplicateTabs.setShortcut("")
        self.actionCloseDuplicateTabs.setStatusTip("")
        
        
        self.actionTabOptions = QtWidgets.QAction(self)
        self.actionTabOptions.setObjectName("actionTabOptions")
        self.actionTabOptions.setText("&Close Tab Options")
        self.actionTabOptions.setShortcut("")
        self.actionTabOptions.setStatusTip("")
        
        
        self.actionSwitchToNextTab = QtWidgets.QAction(self)
        self.actionSwitchToNextTab.setObjectName("actionSwitchToNextTab")
        self.actionSwitchToNextTab.setText("&Switch to Next Tab")
        self.actionSwitchToNextTab.setShortcut("Ctrl+Tab")
        self.actionSwitchToNextTab.setStatusTip("")
        
        self.actionSwitchToPreviousTab = QtWidgets.QAction(self)
        self.actionSwitchToPreviousTab.setObjectName("actionSwitchToPreviousTab")
        self.actionSwitchToPreviousTab.setText("&Switch to Previous Tab")
        self.actionSwitchToPreviousTab.setShortcut("Ahift+Ctrl+Tab")
        self.actionSwitchToPreviousTab.setStatusTip("")
        
        self.actionSaveTabsToFile = QtWidgets.QAction(self)
        self.actionSaveTabsToFile.setObjectName("actionSaveTabsToFile")
        self.actionSaveTabsToFile.setText("&Save Tabs to File")
        self.actionSaveTabsToFile.setShortcut("")
        self.actionSaveTabsToFile.setStatusTip("")
        
        self.actionLoadTabsFromFile = QtWidgets.QAction(self)
        self.actionLoadTabsFromFile.setObjectName("actionLoadTabsFromFile")
        self.actionLoadTabsFromFile.setText("&Load Tabs From File")
        self.actionLoadTabsFromFile.setShortcut("")
        self.actionLoadTabsFromFile.setStatusTip("")
        
        self.actionSaveCurrentTabsToNewFavoriteTabs = QtWidgets.QAction(self)
        self.actionSaveCurrentTabsToNewFavoriteTabs.setObjectName("actionSaveCurrentTabsToNewFavoriteTabs")
        self.actionSaveCurrentTabsToNewFavoriteTabs.setText("&Save Current Tabs to New Favorite Tabs")
        self.actionSaveCurrentTabsToNewFavoriteTabs.setShortcut("")
        self.actionSaveCurrentTabsToNewFavoriteTabs.setStatusTip("")
        
        self.actionLoadTabsFromFavoriteTabs = QtWidgets.QAction(self)
        self.actionLoadTabsFromFavoriteTabs.setObjectName("actionLoadTabsFromFavoriteTabs")
        self.actionLoadTabsFromFavoriteTabs.setText("&Load Tabs From Favorite Tabs")
        self.actionLoadTabsFromFavoriteTabs.setShortcut("")
        self.actionLoadTabsFromFavoriteTabs.setStatusTip("")
        
        self.actionConfigurationOfFolderTabs = QtWidgets.QAction(self)
        self.actionConfigurationOfFolderTabs.setObjectName("actionConfigurationOfFolderTabs")
        self.actionConfigurationOfFolderTabs.setText("&Configuration Of Folder Tabs")
        self.actionConfigurationOfFolderTabs.setShortcut("")
        self.actionConfigurationOfFolderTabs.setStatusTip("")
        
        self.actionConfigurationOfFavoriteTabs = QtWidgets.QAction(self)
        self.actionConfigurationOfFavoriteTabs.setObjectName("actionConfigurationOfFavoriteTabs")
        self.actionConfigurationOfFavoriteTabs.setText("&Configuration Of Favorite Tabs")
        self.actionConfigurationOfFavoriteTabs.setShortcut("")
        self.actionConfigurationOfFavoriteTabs.setStatusTip("")
        
        self.actionNormal = QtWidgets.QAction(self)
        self.actionNormal.setObjectName("actionNormal")  
        self.actionNormal.setText("&Normal")
        self.actionNormal.setShortcut("")
        self.actionNormal.setStatusTip("")
        
        self.actionLocked = QtWidgets.QAction(self)
        self.actionLocked.setObjectName("actionLocked")
        self.actionLocked.setText("&Locked")
        self.actionLocked.setShortcut("")
        self.actionLocked.setStatusTip("")
        
        self.actionLockedWithDirectoryChangesAllowed = QtWidgets.QAction(self)
        self.actionLockedWithDirectoryChangesAllowed.setObjectName("actionLockedWithDirectoryChangesAllowed")
        self.actionLockedWithDirectoryChangesAllowed.setText("&Locked With Directory Changes Allowed")
        self.actionLockedWithDirectoryChangesAllowed.setShortcut("")
        self.actionLockedWithDirectoryChangesAllowed.setStatusTip("")
        
        self.actionLockedWithDirectoriesOpenedInNewTabs = QtWidgets.QAction(self)
        self.actionLockedWithDirectoriesOpenedInNewTabs.setObjectName("actionLockedWithDirectoriesOpenedInNewTabs")
        self.actionLockedWithDirectoriesOpenedInNewTabs.setText("&Locked With Directories Opened In New Tabs")
        self.actionLockedWithDirectoriesOpenedInNewTabs.setShortcut("")
        self.actionLockedWithDirectoriesOpenedInNewTabs.setStatusTip("")
        
        self.actionSetAllTabsToNormal = QtWidgets.QAction(self)
        self.actionSetAllTabsToNormal.setObjectName("actionSetAllTabsToNormal")
        self.actionSetAllTabsToNormal.setText("&Set All Tabs To Normal")
        self.actionSetAllTabsToNormal.setShortcut("")
        self.actionSetAllTabsToNormal.setStatusTip("")
        
        self.actionSetAllTabsToLocked = QtWidgets.QAction(self)
        self.actionSetAllTabsToLocked.setObjectName("actionSetAllTabsToLocked")
        self.actionSetAllTabsToLocked.setText("&Set All Tabs To Locked")
        self.actionSetAllTabsToLocked.setShortcut("")
        self.actionSetAllTabsToLocked.setStatusTip("")
        
        self.actionAllTabsLockedWithDirChangesAllowed = QtWidgets.QAction(self)
        self.actionAllTabsLockedWithDirChangesAllowed.setObjectName("actionAllTabsLockedWithDirChangesAllowed")
        self.actionAllTabsLockedWithDirChangesAllowed.setText("&All Tabs Locked With Dir Changes Allowed")
        self.actionSetAllTabsToLocked.setShortcut("")
        self.actionSetAllTabsToLocked.setStatusTip("")
        
        self.actionAllTabsLockedWithDirOpenedInNewTabs = QtWidgets.QAction(self)
        self.actionAllTabsLockedWithDirOpenedInNewTabs.setObjectName("actionAllTabsLockedWithDirOpenedInNewTabs")
        self.actionAllTabsLockedWithDirOpenedInNewTabs.setText("&All Tabs Locked With Dir Opened In New Tabs")
        self.actionSetAllTabsToLocked.setShortcut("")
        self.actionSetAllTabsToLocked.setStatusTip("")
        
        ###########################################
       
        self.actionSaveCurrentTabsToNewFavoriteTabs = QtWidgets.QAction(self)
        self.actionSaveCurrentTabsToNewFavoriteTabs.setObjectName("actionSaveCurrentTabsToNewFavoriteTabs")
        self.actionSaveCurrentTabsToNewFavoriteTabs.setText("&Save current tabs to a New Favorite Tabs")
        self.actionSaveCurrentTabsToNewFavoriteTabs.setShortcut("")
        self.actionSaveCurrentTabsToNewFavoriteTabs.setStatusTip("")
        
        self.actionResaveOnTheLastFavoriteTabsLoaded = QtWidgets.QAction(self)
        self.actionResaveOnTheLastFavoriteTabsLoaded.setObjectName("actionResaveOnTheLastFavoriteTabsLoaded")
        self.actionResaveOnTheLastFavoriteTabsLoaded.setText("&Resave on the last Favorite Tabs loaded")
        self.actionResaveOnTheLastFavoriteTabsLoaded.setShortcut("")
        self.actionResaveOnTheLastFavoriteTabsLoaded.setStatusTip("")
        
        self.actionRelopadTheLastFavoriteTabsLoaded = QtWidgets.QAction(self)
        self.actionRelopadTheLastFavoriteTabsLoaded.setObjectName("actionRelopadTheLastFavoriteTabsLoaded")
        self.actionRelopadTheLastFavoriteTabsLoaded.setText("&Relopad the last Favorite Tabs loaded")
        self.actionRelopadTheLastFavoriteTabsLoaded.setShortcut("")
        self.actionRelopadTheLastFavoriteTabsLoaded.setStatusTip("")
        
        self.actionConfigurationOfFavoriteTabs = QtWidgets.QAction(self)
        self.actionConfigurationOfFavoriteTabs.setObjectName("actionConfigurationOfFavoriteTabs2")
        self.actionConfigurationOfFavoriteTabs.setText("&Configuration of Favorite Tabs")
        self.actionConfigurationOfFavoriteTabs.setShortcut("")
        self.actionConfigurationOfFavoriteTabs.setStatusTip("")
        
        self.actionBriefView = QtWidgets.QAction(self)
        self.actionBriefView.setObjectName("actionBriefView")
        self.actionBriefView.setText("&Brief View")
        self.actionBriefView.setShortcut("Ctrl+F1")
        self.actionBriefView.setStatusTip("")
        
        self.actionFull = QtWidgets.QAction(self)
        self.actionFull.setObjectName("actionFull")
        self.actionFull.setText("&Full")
        self.actionFull.setShortcut("Ctrl+F2")
        self.actionFull.setStatusTip("")
       
        self.actionThumbnails = QtWidgets.QAction(self)
        self.actionThumbnails.setObjectName("actionThumbnails")
        self.actionThumbnails.setText("&Thumbnails")
        self.actionThumbnails.setShortcut("Shift+Ctrl+F1")
        self.actionThumbnails.setStatusTip("")
        
        self.actionQuickViewPanel = QtWidgets.QAction(self)
        self.actionQuickViewPanel.setObjectName("actionQuickViewPanel")
        self.actionQuickViewPanel.setText("&Quick View Panel")
        self.actionQuickViewPanel.setShortcut("Ctrl+Q")
        self.actionQuickViewPanel.setStatusTip("")
        
        self.actionTreeViewPanel = QtWidgets.QAction(self)
        self.actionTreeViewPanel.setObjectName("actionTreeViewPanel")
        self.actionTreeViewPanel.setText("&Tree View Panel")
        self.actionTreeViewPanel.setShortcut("Shift+Ctrl+F8")
        self.actionTreeViewPanel.setStatusTip("")
        
        self.actionSortByName = QtWidgets.QAction(self)
        self.actionSortByName.setObjectName("actionSortByName")
        self.actionSortByName.setText("&Sort By Name")
        self.actionSortByName.setShortcut("Ctrl+F3")
        self.actionSortByName.setStatusTip("")
        
        self.actionSortByExtension = QtWidgets.QAction(self)
        self.actionSortByExtension.setObjectName("actionSortByExtension")
        self.actionSortByExtension.setText("&Sort By Extension")
        self.actionSortByExtension.setShortcut("Ctrl+F4")
        self.actionSortByExtension.setStatusTip("")
        
        self.actionSortBySize = QtWidgets.QAction(self)
        self.actionSortBySize.setObjectName("actionSortBySize")
        self.actionSortBySize.setText("&Sort By Size")
        self.actionSortBySize.setShortcut("Ctrl+F6")
        self.actionSortBySize.setStatusTip("")
        
        self.actionSortByDate = QtWidgets.QAction(self)
        self.actionSortByDate.setObjectName("actionSortByDate")
        self.actionSortByDate.setText("&Sort By Date")
        self.actionSortByDate.setShortcut("Ctrl+F5")
        self.actionSortByDate.setStatusTip("")
        
        self.actionSortByAttributes = QtWidgets.QAction(self)
        self.actionSortByAttributes.setObjectName("actionSortByAttributes")
        self.actionSortByAttributes.setText("&Sort By Attributes")
        self.actionSortByAttributes.setShortcut("")
        self.actionSortByAttributes.setStatusTip("")
        
        self.actionReverseOrder = QtWidgets.QAction(self)
        self.actionReverseOrder.setObjectName("actionReverseOrder")
        self.actionReverseOrder.setText("&Reverse Order")
        self.actionReverseOrder.setShortcut("")
        self.actionReverseOrder.setStatusTip("")
        
        self.actionRefresh = QtWidgets.QAction(self)
        self.actionRefresh.setObjectName("actionRefresh")
        self.actionRefresh.setText("&Refresh")
        self.actionRefresh.setShortcut("Ctrl+R")
        self.actionRefresh.setStatusTip("")
        
        self.actionShowHiddenSystemFiles = QtWidgets.QAction(self)
        self.actionShowHiddenSystemFiles.setObjectName("actionShowHiddenSystemFiles")
        self.actionShowHiddenSystemFiles.setText("&Show Hidden System Files")
        self.actionShowHiddenSystemFiles.setShortcut("Ctrl+NumDot")
        self.actionShowHiddenSystemFiles.setStatusTip("")
        
        self.actionHorizontalPanelsMode = QtWidgets.QAction(self)
        self.actionHorizontalPanelsMode.setObjectName("actionHorizontalPanelsMode")
        self.actionHorizontalPanelsMode.setText("&Horizontal Panels Mode")
        self.actionHorizontalPanelsMode.setShortcut("Shift+Ctrl+H")
        self.actionHorizontalPanelsMode.setStatusTip("")
        
        self.actionOperationsViewer = QtWidgets.QAction(self)
        self.actionOperationsViewer.setObjectName("actionOperationsViewer")
        self.actionOperationsViewer.setText("&Operations Viewer")
        self.actionOperationsViewer.setShortcut("Alt+V")
        self.actionOperationsViewer.setStatusTip("")
       
       
        
        self.actionOptions = QtWidgets.QAction(self)
        self.actionOptions.setObjectName("actionOptions")
        self.actionOptions.setText("&Options...")
        self.actionOptions.setShortcut("")
        self.actionOptions.setStatusTip("")
        
        self.actionConfigurationOfDirectoryHotlist = QtWidgets.QAction(self)
        self.actionConfigurationOfDirectoryHotlist.setObjectName("actionConfigurationOfDirectoryHotlist")
        self.actionConfigurationOfDirectoryHotlist.setText("&Configuration of Directory Hotlist")
        self.actionConfigurationOfDirectoryHotlist.setShortcut("Shift+Ctrl+D")
        self.actionConfigurationOfDirectoryHotlist.setStatusTip("")
        
        '''self.actionConfigurationOfFavoriteTabs4 = QtWidgets.QAction(self)
        self.actionConfigurationOfFavoriteTabs4.setObjectName("actionConfigurationOfFavoriteTabs4")
        self.actionCreateSymbolicLink.setText("&Save Selection")'''
        
        self.actionConfigurationOfFileAssociations = QtWidgets.QAction(self)
        self.actionConfigurationOfFileAssociations.setObjectName("actionConfigurationOfFileAssociations")
        self.actionConfigurationOfFileAssociations.setText("&Configuration of File Associations")
        self.actionConfigurationOfFileAssociations.setShortcut("")
        self.actionConfigurationOfFileAssociations.setStatusTip("")
        
        self.actionConfigurationOfFolderTabs = QtWidgets.QAction(self)
        self.actionConfigurationOfFolderTabs.setObjectName("actionConfigurationOfFolderTabs")
        self.actionCreateSymbolicLink.setText("&Configuration of Folder Tabs")
        
        self.actionConfigurationOfArchivers = QtWidgets.QAction(self)
        self.actionConfigurationOfArchivers.setObjectName("actionConfigurationOfArchivers")
        self.actionConfigurationOfArchivers.setText("&Configuration of Archivers")
        self.actionConfigurationOfArchivers.setShortcut("")
        self.actionConfigurationOfArchivers.setStatusTip("")
        
        self.actionSavePosition = QtWidgets.QAction(self)
        self.actionSavePosition.setObjectName("actionSavePosition")
        self.actionSavePosition.setText("&Save Position")
        self.actionSavePosition.setShortcut("")
        self.actionSavePosition.setStatusTip("")
        
        self.actionSaveSettings = QtWidgets.QAction(self)
        self.actionSaveSettings.setObjectName("actionSaveSettings")
        self.actionSaveSettings.setText("&Save Settings")
        self.actionSaveSettings.setShortcut("")
        self.actionSaveSettings.setStatusTip("")
        
        self.actionContents = QtWidgets.QAction(self)
        self.actionContents.setObjectName("actionContents")
        self.actionContents.setText("&Contents")
        self.actionContents.setShortcut("")
        self.actionContents.setStatusTip("")
        
        self.actionKeyboard = QtWidgets.QAction(self)
        self.actionKeyboard.setObjectName("actionKeyboard")
        self.actionKeyboard.setText("&Keyboard")
        self.actionKeyboard.setShortcut("")
        self.actionKeyboard.setStatusTip("")
        
        self.actionVisitDoubleCommanderWebsite = QtWidgets.QAction(self)
        self.actionVisitDoubleCommanderWebsite.setObjectName("actionVisitDoubleCommanderWebsite")
        self.actionVisitDoubleCommanderWebsite.setText("&Visit Double Commander Website")
        self.actionVisitDoubleCommanderWebsite.setShortcut("")
        self.actionVisitDoubleCommanderWebsite.setStatusTip("")
        
        self.actionAbout = QtWidgets.QAction(self)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.setText("&About")
        self.actionAbout.setShortcut("")
        self.actionAbout.setStatusTip("")
        #C:/Users/Yevhen_Vieskov/pyCommander/pyCommander/pixmaps/dctheme/16x16/actions/application-exit.png
        
        path_abs = os.path.dirname(__file__)
        path_pixmap = "pixmaps/dctheme/16x16/actions"
        path = os.path.join(path_abs, path_pixmap)
        self.actionTBRefresh = QtWidgets.QAction(self)
        icon_refresh = QtGui.QIcon()
        icon_refresh.addPixmap(QtGui.QPixmap(os.path.join(path, "cm_refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon_refresh.addPixmap(QtGui.QPixmap(os.path.join(path, "cm_refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionTBRefresh.setIcon(icon_refresh)
        self.actionTBRefresh.setObjectName("actionTBRefresh")
        self.actionTBRunTerminal = QtWidgets.QAction(self)
        icon_runterm = QtGui.QIcon()
        icon_runterm.addPixmap(QtGui.QPixmap(os.path.join(path, "cm_runterm.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionTBRunTerminal.setIcon(icon_runterm)
        self.actionTBRunTerminal.setObjectName("actionTBRunTerminal")
        self.actionTBOptions = QtWidgets.QAction(self)
        icon_options = QtGui.QIcon()
        icon_options.addPixmap(QtGui.QPixmap(os.path.join(path, "cm_options.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionTBOptions.setIcon(icon_options)
        self.actionTBOptions.setObjectName("actionTBOptions")
        self.actionTBBriefView = QtWidgets.QAction(self)
        self.actionTBBriefView.setCheckable(True)
        icon_briefview = QtGui.QIcon()
        icon_briefview.addPixmap(QtGui.QPixmap(os.path.join(path, "cm_briefview.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon_briefview.addPixmap(QtGui.QPixmap("cm_briefview.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionTBBriefView.setIcon(icon_briefview)
        self.actionTBBriefView.setObjectName("actionTBBriefView")
        self.actionTBColumnsView = QtWidgets.QAction(self)
        self.actionTBColumnsView.setCheckable(True)
        icon_columnsview = QtGui.QIcon()
        icon_columnsview.addPixmap(QtGui.QPixmap(os.path.join(path, "cm_columnsview.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionTBColumnsView.setIcon(icon_columnsview)
        self.actionTBColumnsView.setObjectName("actionTBColumnsView")
        self.actionTBThumbnails = QtWidgets.QAction(self)
        self.actionTBThumbnails.setCheckable(True)
        icon_thumbnailsview = QtGui.QIcon()
        icon_thumbnailsview.addPixmap(QtGui.QPixmap(os.path.join(path, "cm_thumbnailsview.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionTBThumbnails.setIcon(icon_thumbnailsview)
        self.actionTBThumbnails.setObjectName("actionTBThumbnails")
        self.actionTBFlatView = QtWidgets.QAction(self)
        self.actionTBFlatView.setCheckable(True)
        icon_flatview = QtGui.QIcon()
        icon_flatview.addPixmap(QtGui.QPixmap(os.path.join(path, "cm_flatview.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionTBFlatView.setIcon(icon_flatview)
        self.actionTBFlatView.setObjectName("actionTBFlatView")
        self.actionTBGotoPreviousEntryInHistory = QtWidgets.QAction(self)
        icon_viewhistoryprev = QtGui.QIcon()
        icon_viewhistoryprev.addPixmap(QtGui.QPixmap(os.path.join(path, "cm_viewhistoryprev.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionTBGotoPreviousEntryInHistory.setIcon(icon_viewhistoryprev)
        self.actionTBGotoPreviousEntryInHistory.setObjectName("actionTBGotoPreviousEntryInHistory")
        self.actionTBGotoPreviousEntryInHistory2 = QtWidgets.QAction(self)
        icon_viewhistorynext = QtGui.QIcon()
        icon_viewhistorynext.addPixmap(QtGui.QPixmap(os.path.join(path, "cm_viewhistorynext.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionTBGotoPreviousEntryInHistory2.setIcon(icon_viewhistorynext)
        self.actionTBGotoPreviousEntryInHistory2.setObjectName("actionTBGotoPreviousEntryInHistory2")
        self.actionTBSelectGroup = QtWidgets.QAction(self)
        icon_markplus = QtGui.QIcon()
        icon_markplus.addPixmap(QtGui.QPixmap(os.path.join(path, "cm_markplus.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionTBSelectGroup.setIcon(icon_markplus)
        self.actionTBSelectGroup.setObjectName("actionTBSelectGroup")
        self.actionTBUnselectGroup = QtWidgets.QAction(self)
        icon_markminus = QtGui.QIcon()
        icon_markminus.addPixmap(QtGui.QPixmap(os.path.join(path, "cm_markminus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon_markminus.addPixmap(QtGui.QPixmap(os.path.join(path,"cm_markplus.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionTBUnselectGroup.setIcon(icon_markminus)
        self.actionTBUnselectGroup.setObjectName("actionTBUnselectGroup")
        self.actionTBInvertSelection = QtWidgets.QAction(self)
        icon_markinvert = QtGui.QIcon()
        icon_markinvert.addPixmap(QtGui.QPixmap(os.path.join(path, "cm_markinvert.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon_markinvert.addPixmap(QtGui.QPixmap(os.path.join(path, "cm_markplus.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionTBInvertSelection.setIcon(icon_markinvert)
        self.actionTBInvertSelection.setObjectName("actionTBInvertSelection")
        self.actionTBPackFiles = QtWidgets.QAction(self)
        icon_packfiles = QtGui.QIcon()
        icon_packfiles.addPixmap(QtGui.QPixmap(os.path.join(path, "cm_packfiles.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionTBPackFiles.setIcon(icon_packfiles)
        self.actionTBPackFiles.setObjectName("actionTBPackFiles")
        self.actionTBExtractFiles = QtWidgets.QAction(self)
        icon_extractfiles = QtGui.QIcon()
        icon_extractfiles.addPixmap(QtGui.QPixmap(os.path.join(path,"cm_extractfiles.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionTBExtractFiles.setIcon(icon_extractfiles)
        self.actionTBExtractFiles.setObjectName("actionTBExtractFiles")
        self.actionTBSearch = QtWidgets.QAction(self)
        icon_search = QtGui.QIcon()
        icon_search.addPixmap(QtGui.QPixmap(os.path.join(path, "cm_search.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionTBSearch.setIcon(icon_search)
        self.actionTBSearch.setObjectName("actionTBSearch")
        self.actionTBMultiRenameTool = QtWidgets.QAction(self)
        icon_multirename = QtGui.QIcon()
        icon_multirename.addPixmap(QtGui.QPixmap(os.path.join(path, "cm_multirename.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionTBMultiRenameTool.setIcon(icon_multirename)
        self.actionTBMultiRenameTool.setObjectName("actionTBMultiRenameTool")
        self.actionTBSynchronizeDirs = QtWidgets.QAction(self)
        icon_syncdirs = QtGui.QIcon()
        icon_syncdirs.addPixmap(QtGui.QPixmap(os.path.join(path, "cm_syncdirs.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionTBSynchronizeDirs.setIcon(icon_syncdirs)
        self.actionTBSynchronizeDirs.setObjectName("actionTBSynchronizeDirs")
        self.actionTBCopyFilenameWithFullPath = QtWidgets.QAction(self)
        icon_copyfullnamestoclip = QtGui.QIcon()
        icon_copyfullnamestoclip.addPixmap(QtGui.QPixmap(os.path.join(path, "cm_copyfullnamestoclip.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionTBCopyFilenameWithFullPath.setIcon(icon_copyfullnamestoclip)
        self.actionTBCopyFilenameWithFullPath.setObjectName("actionTBCopyFilenameWithFullPath")
    
    def _connectActions(self):
        self.actionCreateSymbolicLink.triggered.connect(self.create_symbolic_link)
        self.actionCreateHardLink.triggered.connect(self.create_hard_link)
        self.actionCreateDirectory.triggered.connect(self.create_directory)
        self.actionCreateShortcut.triggered.connect(self.create_shortcut)
        self.actionChangeAttributes.triggered.connect(self.change_attributes)
        self.actionShowFileProperties.triggered.connect(self.show_file_properties)
        self.actionEditComment.triggered.connect(self.edit_comment)
        self.actionCalculateOccupiedSpace.triggered.connect(self.calculate_occupied_space)
        self.actionCompareByContents.triggered.connect(self.compare_by_contents)
        self.actionMultiRenameTool.triggered.connect(self.multi_rename_tool)
        self.actionPackFiles.triggered.connect(self.pack_files)
        self.actionExtractFiles.triggered.connect(self.extract_files)
        self.actionTestArchive.triggered.connect(self.test_archive)
        self.actionSplitFile.triggered.connect(self.split_file)
        self.actionCombineFiles.triggered.connect(self.combine_file)
        self.actionCalculateChecksum.triggered.connect(self.calculate_checksaum)
        self.actionVerifyChecksum.triggered.connect(self.verify_checksum)
        self.actionWipe.triggered.connect(self.wipe)
        self.actionDelete.triggered.connect(self.pc_delete)
        self.actionExit.triggered.connect(self.pc_exit)
        
        self.actionSelectGroup.triggered.connect(self.select_group)
        self.actionUnselectGroup.triggered.connect(self.unselect_group)
        self.actionSelectAll.triggered.connect(self.select_all)
        self.actionUnselectAll.triggered.connect(self.unselect_all)
        self.actionInvertSelection.triggered.connect(self.invert_selection)
        self.actionSelectAllWithTheSameExtension.triggered.connect(self.select_all_with_the_same_extension)        
        self.actionSaveSelection.triggered.connect(self.save_selection)
        self.actionRestoreSelection.triggered.connect(self.restore_selection)
        self.actionSaveSelectionToFile.triggered.connect(self.save_selection_to_file)
        self.actionLoadSelectionFromFile.triggered.connect(self.load_selection_from_file)
        self.actionLoadSelectionFromClipboard.triggered.connect(self.load_selection_from_clipboard)        
        self.actionCopyFilenameToClipboard.triggered.connect(self.copy_filename_to_clipboard)
        self.actionCopyFilenameWithFullPath.triggered.connect(self.copy_filename_with_full_path)
        self.actionCopyAllShownColumns.triggered.connect(self.copy_all_shown_columns)        
        self.actionCompareDirectories.triggered.connect(self.compare_directories)
        
        self.actionSearch.triggered.connect(self.search)
        self.actionNewSearchInstance.triggered.connect(self.search_instance)
        self.actionViewCurrentSearchInstances.triggered.connect(self.current_search_instances)
        self.actionDirectoryHotlist.triggered.connect(self.directory_hot_list)
        self.actionSynchronizeDirs.triggered.connect(self.synchronize_dirs)       
        self.actionRunTerminal.triggered.connect(self.run_terminal)
        self.actionExecuteInternalCommand.triggered.connect(self.execute_internal_command)        
        self.actionFlatView.triggered.connect(self.flat_view)
        self.actionOpenVFSList.triggered.connect(self.open_vfs_list)
        self.actionSwapPanels.triggered.connect(self.swap_panels)
        self.actionTargetSource.triggered.connect(self.target_source)        
        self.actionShowOccupiedSpace.triggered.connect(self.show_occupied_space)
        
        self.actionNetworkConnect.triggered.connect(self.network_connect)
        self.actionNetworkDisconnect.triggered.connect(self.network_disconnect)       
        self.actionMapNetworkDrive.triggered.connect(self.map_network_drive)
        self.actionDisconnectNetworkDrive.triggered.connect(self.disconnect_network_drive)      
        self.actionCopyNamesWithUNCPath.triggered.connect(self.copy_names_with_uncpath)
        
        self.actionNewTab.triggered.connect(self.new_tab)
        self.actionRenameTab.triggered.connect(self.rename_tab)
        self.actionOpenFolderInNewTab.triggered.connect(self.open_folder_in_new_tab)       
        self.actionCloseTab.triggered.connect(self.close_tab)        
        self.actionCloseDuplicateTabs.triggered.connect(self.close_duplicated_tab)
        normal
       self.actionNormal.triggered.connect(self.normal) 
       self.actionLocked.triggered.connect(self.locked)
       self.actionLockedWithDirectoryChangesAllowed.triggered.connect(self.locked_with_directory_changes_allowed)
       self.actionLockedWithDirectoriesOpenedInNewTabs.triggered.connect(self.locked_with_directories_opened_in_new_tabs)       
       self.actionSetAllTabsToNormal.triggered.connect(self.set_all_tabs_to_normal) 
       self.actionSetAllTabsToLocked.triggered.connect(self.set_all_tabs_to_locked)
       self.actionAllTabsLockedWithDirChangesAllowed.triggered.connect(self.all_tabs_locked_with_dir_changes_allowed)
       self.actionAllTabsLockedWithDirOpenedInNewTabs.triggered.connect(self.all_tabs_locked_with_dir_opened_in_new_tabs)
       
       self.actionSwitchToNextTab.triggered.connect(self.switch_to_next_tab)
       self.actionSwitchToPreviousTab.triggered.connect(self.switch_to_previous_tab)
        
       self.actionSaveTabsToFile.triggered.connect(self.save_tabs_to_file)
       self.actionLoadTabsFromFile.triggered.connect(self.load_tabs_from_file)
       self.actionSaveCurrentTabsToNewFavoriteTabs.triggered.connect(self.save_current_tabs_to_new_favorite_tabs)
       self.actionLoadTabsFromFavoriteTabs.triggered.connect(self.load_tabs_from_favorite_tabs)
        
       self.actionConfigurationOfFolderTabs.triggered.connect(self.configuration_of_folder_tabs)
       self.actionConfigurationOfFavoriteTabs.triggered.connect(self.configuration_of_favorite_tabs)       
       
       self.actionSaveCurrentTabsToNewFavoriteTabs.triggered.connect(self.save_current_tabs_to_new_favorite_tabs)
       self.actionResaveOnTheLastFavoriteTabsLoaded.triggered.connect(self.resave_on_the_last_favorite_tabs_loaded)
       self.actionRelopadTheLastFavoriteTabsLoaded.triggered.connect(self.relopad_the_last_favorite_tabs_loaded)
       self.actionConfigurationOfFavoriteTabs.triggered.connect(self.configuration_of_favorite_tabs)
    
       self.actionBriefView.triggered.connect(self.brief_view)
       self.actionFull.triggered.connect(self.full)
       self.actionThumbnails.triggered.connect(self.thumbnails)        
       self.actionQuickViewPanel.triggered.connect(self.quick_view_panel)
       self.actionTreeViewPanel.triggered.connect(self.tree_view_panel)        
       self.actionSortByName.triggered.connect(self.sort_by_name)
       self.actionSortByExtension.triggered.connect(self.sort_by_extension)
       self.actionSortBySize.triggered.connect(self.sort_by_size)
       self.actionSortByDate.triggered.connect(self.sort_by_date)
       self.actionSortByAttributes.triggered.connect(self.sort_by_attributes)        
       self.actionReverseOrder.triggered.connect(self.reverse_order)
       self.actionRefresh.triggered.connect(self.refresh)        
       self.actionShowHiddenSystemFiles.triggered.connect(self.show_hidden_system_files)        
       self.actionHorizontalPanelsMode.triggered.connect(self.horizontal_panels_mode)       
       self.actionOperationsViewer.triggered.connect(self.operations_viewer)
       
       self.actionOptionsTriggered.connect(self.options_triggered)        
       self.actionConfigurationOfDirectoryHotlist.triggered.connect(self.configuration_of_directory_hotlist)
       self.actionConfigurationOfFileAssociations.triggered.connect(self.configuration_of_file_associations)
       self.actionConfigurationOfArchivers.triggered.connect(self.configuration_of_archivers)
       self.actionSavePosition.triggered.connect(self.save_position)
       self.actionSaveSettings.triggered.connect(self.save_settings)
       
       self.actionContents.triggered.connect(self.contents)
       self.actionKeyboard.triggered.connect(self.keyboard)
       self.actionVisitDoubleCommanderWebsite.triggered.connect(self.visit_double_commander_website)    
       self.actionAbout.triggered.connect(self.about)
  
    
    def _createToolBars(self):
        self.toolBar = QtWidgets.QToolBar(self)
        self.toolBar.setObjectName("mainToolBar")
        self.toolBar.setIconSize(QtCore.QSize(16,16))
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar.addAction(self.actionTBRefresh)
        self.toolBar.addAction(self.actionTBRunTerminal)
        self.toolBar.addAction(self.actionTBOptions)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionTBBriefView)
        self.toolBar.addAction(self.actionTBColumnsView)
        self.toolBar.addAction(self.actionTBThumbnails)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionTBFlatView)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionTBGotoPreviousEntryInHistory)
        self.toolBar.addAction(self.actionTBGotoPreviousEntryInHistory2)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionTBSelectGroup)
        self.toolBar.addAction(self.actionTBUnselectGroup)
        self.toolBar.addAction(self.actionTBInvertSelection)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionTBPackFiles)
        self.toolBar.addAction(self.actionTBExtractFiles)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionTBSearch)
        self.toolBar.addAction(self.actionTBMultiRenameTool)
        self.toolBar.addAction(self.actionTBSynchronizeDirs)
        self.toolBar.addAction(self.actionTBCopyFilenameWithFullPath)
        

    def create_symbolic_link():
        pass
    def create_hard_link():
        pass
    def create_directory():
        pass
    def create_shortcut():
        pass
    def change_attributes():
        pass
    def show_file_properties():
        pass
    def edit_comment():
        pass
    def calculate_occupied_space():
        pass
    def compare_by_contents():
        pass
    def multi_rename_tool():
        pass
    def pack_files():
        pass
    def extract_files():
        pass
    def test_archive():
        pass
    def split_file():
        pass
    def combine_file():
        pass
    def calculate_checksaum():
        pass
    def verify_checksum():
        pass
    def wipe():
        pass
    def pc_delete():
        pass
    def pc_exit():
        pass
    
    def select_group():
        pass
    def unselect_group():
        pass
    def select_all():
        pass
    def unselect_all():
        pass
    def invert_selection():
        pass
    def select_all_with_the_same_extension():
        pass
    def restore_selection():
        pass
    def save_selection_to_file():
        pass
    def load_selection_from_file():
        pass
    def load_selection_from_clipboard():
        pass
    def copy_filename_to_clipboard():
        pass
    def copy_filename_with_full_path():
        pass
    def copy_all_shown_columns():
        pass
    def compare_directories(): 
        pass
    
    def search():
        pass
    def search_instance():
        pass
    def current_search_instances():
        pass
    def directory_hot_list():
        pass
    def synchronize_dirs():
        pass
    def run_terminal():
        pass
    def execute_internal_command():
        pass
    def flat_view():
        pass
    def open_vfs_list():
        pass
    def swap_panels():
        pass
    def target_source():
        pass
    def show_occupied_space():
        pass

    def network_connect():
        pass
    def network_disconnect():
        pass
    def map_network_drive():
        pass
    def disconnect_network_drive():
        pass
    def copy_names_with_uncpath():
        pass
    def new_tab():
        pass
    def rename_tab():
        pass
    def open_folder_in_new_tab():
        pass
    def close_tab():
        pass
    def close_duplicated_tab():
        pass
    def normal():
        pass
    def locked():
        pass
    def locked_with_directory_changes_allowed():
        pass
    def locked_with_directories_opened_in_new_tabs():
        pass
    def set_all_tabs_to_normal():
        pass
    def set_all_tabs_to_locked():
        pass
    def all_tabs_locked_with_dir_changes_allowed():
        pass
    def all_tabs_locked_with_dir_opened_in_new_tabs():
        pass
    def switch_to_next_tab():
        pass
    def switch_to_previous_tab():
        pass
    def save_tabs_to_file():
        pass
    def load_tabs_from_file():
        pass
    def save_current_tabs_to_new_favorite_tabs():
        pass
    def load_tabs_from_favorite_tabs():
        pass
    def configuration_of_folder_tabs():
        pass
    def configuration_of_favorite_tabs():
        pass
    def save_current_tabs_to_new_favorite_tabs():
        pass
    def resave_on_the_last_favorite_tabs_loaded():
        pass
    def relopad_the_last_favorite_tabs_loaded():
        pass
    def configuration_of_favorite_tabs():
        pass
   def brief_view():
       pass
   def full():
       pass
   def thumbnails():
       pass
   def quick_view_panel():
       pass
   def tree_view_panel():
       pass
   def sort_by_name():
       pass
   def sort_by_extension():
       pass
   def sort_by_size():
       pass
   def sort_by_date():
       pass
   def sort_by_attributes():
       pass
-  def reverse_order():
       pass
   def refresh():
       pass
   def show_hidden_system_files():
       pass
   def horizontal_panels_mode():
       pass
   def operations_viewer():
       pass
   def options_triggered():
       pass
   def configuration_of_directory_hotlist():
       pass
   def configuration_of_file_associations():
       pass
   def configuration_of_archivers():
       pass
   def save_position():
       pass
   def save_settings():
       pass
   def contents():
       pass
   def keyboard():
       pass
   def visit_double_commander_website():
       pass
   def about():
       pass

