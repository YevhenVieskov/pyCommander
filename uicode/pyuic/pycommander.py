# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pycommander.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1143, 745)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 10, 1141, 661))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tabWidget = QtWidgets.QTabWidget(self.widget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.treeView = QtWidgets.QTreeView(self.tab_2)
        self.treeView.setGeometry(QtCore.QRect(0, 0, 351, 391))
        self.treeView.setObjectName("treeView")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_4.addWidget(self.comboBox_2)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.widget)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.treeView_2 = QtWidgets.QTreeView(self.tab_3)
        self.treeView_2.setGeometry(QtCore.QRect(0, 0, 331, 391))
        self.treeView_2.setObjectName("treeView_2")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.verticalLayout_2.addWidget(self.tabWidget_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.fontComboBox = QtWidgets.QFontComboBox(self.widget)
        self.fontComboBox.setObjectName("fontComboBox")
        self.horizontalLayout_2.addWidget(self.fontComboBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1143, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuPrint = QtWidgets.QMenu(self.menuFile)
        self.menuPrint.setObjectName("menuPrint")
        self.menuMark = QtWidgets.QMenu(self.menubar)
        self.menuMark.setObjectName("menuMark")
        self.menuCommands = QtWidgets.QMenu(self.menubar)
        self.menuCommands.setObjectName("menuCommands")
        self.menuNet = QtWidgets.QMenu(self.menubar)
        self.menuNet.setObjectName("menuNet")
        self.menuShow = QtWidgets.QMenu(self.menubar)
        self.menuShow.setObjectName("menuShow")
        self.menuonfiguration = QtWidgets.QMenu(self.menubar)
        self.menuonfiguration.setObjectName("menuonfiguration")
        self.menuStart = QtWidgets.QMenu(self.menubar)
        self.menuStart.setObjectName("menuStart")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionChange_Attributes = QtWidgets.QAction(MainWindow)
        self.actionChange_Attributes.setObjectName("actionChange_Attributes")
        self.actionPack = QtWidgets.QAction(MainWindow)
        self.actionPack.setObjectName("actionPack")
        self.actionUnpack_Specific_Files = QtWidgets.QAction(MainWindow)
        self.actionUnpack_Specific_Files.setObjectName("actionUnpack_Specific_Files")
        self.actionTest_Archive_s = QtWidgets.QAction(MainWindow)
        self.actionTest_Archive_s.setObjectName("actionTest_Archive_s")
        self.actionCompare_by_Content = QtWidgets.QAction(MainWindow)
        self.actionCompare_by_Content.setObjectName("actionCompare_by_Content")
        self.actionAssociate_With = QtWidgets.QAction(MainWindow)
        self.actionAssociate_With.setObjectName("actionAssociate_With")
        self.actionInternal_Associations_pyCommander_only = QtWidgets.QAction(MainWindow)
        self.actionInternal_Associations_pyCommander_only.setObjectName("actionInternal_Associations_pyCommander_only")
        self.actionProperties = QtWidgets.QAction(MainWindow)
        self.actionProperties.setObjectName("actionProperties")
        self.actionCalculate_Occupied_Space = QtWidgets.QAction(MainWindow)
        self.actionCalculate_Occupied_Space.setObjectName("actionCalculate_Occupied_Space")
        self.actionMulti_Rename_Tool = QtWidgets.QAction(MainWindow)
        self.actionMulti_Rename_Tool.setObjectName("actionMulti_Rename_Tool")
        self.actionEdit_Comment = QtWidgets.QAction(MainWindow)
        self.actionEdit_Comment.setObjectName("actionEdit_Comment")
        self.actionFile_List = QtWidgets.QAction(MainWindow)
        self.actionFile_List.setObjectName("actionFile_List")
        self.actionFile_list_with_subdirs = QtWidgets.QAction(MainWindow)
        self.actionFile_list_with_subdirs.setObjectName("actionFile_list_with_subdirs")
        self.actionFile_contents = QtWidgets.QAction(MainWindow)
        self.actionFile_contents.setObjectName("actionFile_contents")
        self.actionSplit_File = QtWidgets.QAction(MainWindow)
        self.actionSplit_File.setObjectName("actionSplit_File")
        self.actionCombine_File = QtWidgets.QAction(MainWindow)
        self.actionCombine_File.setObjectName("actionCombine_File")
        self.actionEncode_File = QtWidgets.QAction(MainWindow)
        self.actionEncode_File.setObjectName("actionEncode_File")
        self.actionDecode_File = QtWidgets.QAction(MainWindow)
        self.actionDecode_File.setObjectName("actionDecode_File")
        self.actionCreate_Checksum_File_s_CRC32_MD5_SHAT = QtWidgets.QAction(MainWindow)
        self.actionCreate_Checksum_File_s_CRC32_MD5_SHAT.setObjectName("actionCreate_Checksum_File_s_CRC32_MD5_SHAT")
        self.actionVerify_Checksum_from_checksum_files = QtWidgets.QAction(MainWindow)
        self.actionVerify_Checksum_from_checksum_files.setObjectName("actionVerify_Checksum_from_checksum_files")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionSelect_Group = QtWidgets.QAction(MainWindow)
        self.actionSelect_Group.setObjectName("actionSelect_Group")
        self.actionUnselect_Group = QtWidgets.QAction(MainWindow)
        self.actionUnselect_Group.setObjectName("actionUnselect_Group")
        self.actionSelect_All = QtWidgets.QAction(MainWindow)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionUnselect_All = QtWidgets.QAction(MainWindow)
        self.actionUnselect_All.setObjectName("actionUnselect_All")
        self.actionInvert_Selection = QtWidgets.QAction(MainWindow)
        self.actionInvert_Selection.setObjectName("actionInvert_Selection")
        self.actionSelect_All_With_Same_Extension = QtWidgets.QAction(MainWindow)
        self.actionSelect_All_With_Same_Extension.setObjectName("actionSelect_All_With_Same_Extension")
        self.actionSave_Selection = QtWidgets.QAction(MainWindow)
        self.actionSave_Selection.setObjectName("actionSave_Selection")
        self.actionRestore_Selection = QtWidgets.QAction(MainWindow)
        self.actionRestore_Selection.setObjectName("actionRestore_Selection")
        self.actionSave_Selection_To_File = QtWidgets.QAction(MainWindow)
        self.actionSave_Selection_To_File.setObjectName("actionSave_Selection_To_File")
        self.actionLoad_Selection_From_File = QtWidgets.QAction(MainWindow)
        self.actionLoad_Selection_From_File.setObjectName("actionLoad_Selection_From_File")
        self.actionCopy_Selected_Names_To_Clipboard = QtWidgets.QAction(MainWindow)
        self.actionCopy_Selected_Names_To_Clipboard.setObjectName("actionCopy_Selected_Names_To_Clipboard")
        self.actionCopy_Names_With_Path_To_Clipboard = QtWidgets.QAction(MainWindow)
        self.actionCopy_Names_With_Path_To_Clipboard.setObjectName("actionCopy_Names_With_Path_To_Clipboard")
        self.actionCopy_To_Clipboard_With_All_Details = QtWidgets.QAction(MainWindow)
        self.actionCopy_To_Clipboard_With_All_Details.setObjectName("actionCopy_To_Clipboard_With_All_Details")
        self.actionCopy_To_Clipboard_With_Path_Details = QtWidgets.QAction(MainWindow)
        self.actionCopy_To_Clipboard_With_Path_Details.setObjectName("actionCopy_To_Clipboard_With_Path_Details")
        self.actionCompare_Directories = QtWidgets.QAction(MainWindow)
        self.actionCompare_Directories.setObjectName("actionCompare_Directories")
        self.actionMark_Newer_Hide_Same_Files = QtWidgets.QAction(MainWindow)
        self.actionMark_Newer_Hide_Same_Files.setObjectName("actionMark_Newer_Hide_Same_Files")
        self.actionCD_Tree = QtWidgets.QAction(MainWindow)
        self.actionCD_Tree.setObjectName("actionCD_Tree")
        self.actionSearch = QtWidgets.QAction(MainWindow)
        self.actionSearch.setObjectName("actionSearch")
        self.actionSearch_in_separate_Process = QtWidgets.QAction(MainWindow)
        self.actionSearch_in_separate_Process.setObjectName("actionSearch_in_separate_Process")
        self.actionVolume_Label = QtWidgets.QAction(MainWindow)
        self.actionVolume_Label.setObjectName("actionVolume_Label")
        self.actionSystem_Information = QtWidgets.QAction(MainWindow)
        self.actionSystem_Information.setObjectName("actionSystem_Information")
        self.actionSynchronize_Dirs = QtWidgets.QAction(MainWindow)
        self.actionSynchronize_Dirs.setObjectName("actionSynchronize_Dirs")
        self.actionDirectory_Hotlist = QtWidgets.QAction(MainWindow)
        self.actionDirectory_Hotlist.setObjectName("actionDirectory_Hotlist")
        self.actionGo_Back = QtWidgets.QAction(MainWindow)
        self.actionGo_Back.setObjectName("actionGo_Back")
        self.actionOpen_command_prompt_window = QtWidgets.QAction(MainWindow)
        self.actionOpen_command_prompt_window.setObjectName("actionOpen_command_prompt_window")
        self.actionBranch_View = QtWidgets.QAction(MainWindow)
        self.actionBranch_View.setObjectName("actionBranch_View")
        self.actionOpen_Desktop_Folder = QtWidgets.QAction(MainWindow)
        self.actionOpen_Desktop_Folder.setObjectName("actionOpen_Desktop_Folder")
        self.actionBackground_Transfer_Manager = QtWidgets.QAction(MainWindow)
        self.actionBackground_Transfer_Manager.setObjectName("actionBackground_Transfer_Manager")
        self.actionSource_Target = QtWidgets.QAction(MainWindow)
        self.actionSource_Target.setObjectName("actionSource_Target")
        self.actionTarget_Source = QtWidgets.QAction(MainWindow)
        self.actionTarget_Source.setObjectName("actionTarget_Source")
        self.actionNetwork_Connections = QtWidgets.QAction(MainWindow)
        self.actionNetwork_Connections.setObjectName("actionNetwork_Connections")
        self.actionDisconnect_Network_Drives = QtWidgets.QAction(MainWindow)
        self.actionDisconnect_Network_Drives.setObjectName("actionDisconnect_Network_Drives")
        self.actionShare_Current_Directory = QtWidgets.QAction(MainWindow)
        self.actionShare_Current_Directory.setObjectName("actionShare_Current_Directory")
        self.actionUnshare_Directory = QtWidgets.QAction(MainWindow)
        self.actionUnshare_Directory.setObjectName("actionUnshare_Directory")
        self.actionShow_Admin_Shares = QtWidgets.QAction(MainWindow)
        self.actionShow_Admin_Shares.setObjectName("actionShow_Admin_Shares")
        self.actionFTP_Connect = QtWidgets.QAction(MainWindow)
        self.actionFTP_Connect.setObjectName("actionFTP_Connect")
        self.actionFTP_New_Connection = QtWidgets.QAction(MainWindow)
        self.actionFTP_New_Connection.setObjectName("actionFTP_New_Connection")
        self.actionFTP_Disconnect = QtWidgets.QAction(MainWindow)
        self.actionFTP_Disconnect.setObjectName("actionFTP_Disconnect")
        self.actionFTP_Show_Hidden_Files = QtWidgets.QAction(MainWindow)
        self.actionFTP_Show_Hidden_Files.setObjectName("actionFTP_Show_Hidden_Files")
        self.actionFTP_Download_From_List = QtWidgets.QAction(MainWindow)
        self.actionFTP_Download_From_List.setObjectName("actionFTP_Download_From_List")
        self.actionPORT_Connection_To_Other_PC = QtWidgets.QAction(MainWindow)
        self.actionPORT_Connection_To_Other_PC.setObjectName("actionPORT_Connection_To_Other_PC")
        self.actionBrief = QtWidgets.QAction(MainWindow)
        self.actionBrief.setObjectName("actionBrief")
        self.actionFull = QtWidgets.QAction(MainWindow)
        self.actionFull.setObjectName("actionFull")
        self.actionComments = QtWidgets.QAction(MainWindow)
        self.actionComments.setObjectName("actionComments")
        self.actionCustom_Columns_Mode = QtWidgets.QAction(MainWindow)
        self.actionCustom_Columns_Mode.setObjectName("actionCustom_Columns_Mode")
        self.actionCustom_View_Modes = QtWidgets.QAction(MainWindow)
        self.actionCustom_View_Modes.setObjectName("actionCustom_View_Modes")
        self.actionTree = QtWidgets.QAction(MainWindow)
        self.actionTree.setObjectName("actionTree")
        self.actionSeparate_Tree = QtWidgets.QAction(MainWindow)
        self.actionSeparate_Tree.setObjectName("actionSeparate_Tree")
        self.actionThumbnail_View = QtWidgets.QAction(MainWindow)
        self.actionThumbnail_View.setObjectName("actionThumbnail_View")
        self.actionQuick_View_Panel = QtWidgets.QAction(MainWindow)
        self.actionQuick_View_Panel.setObjectName("actionQuick_View_Panel")
        self.actionVertical_Arrangement = QtWidgets.QAction(MainWindow)
        self.actionVertical_Arrangement.setObjectName("actionVertical_Arrangement")
        self.actionNew_Folder_Tab = QtWidgets.QAction(MainWindow)
        self.actionNew_Folder_Tab.setObjectName("actionNew_Folder_Tab")
        self.actionAll_Files = QtWidgets.QAction(MainWindow)
        self.actionAll_Files.setObjectName("actionAll_Files")
        self.actionPrograms = QtWidgets.QAction(MainWindow)
        self.actionPrograms.setObjectName("actionPrograms")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.actionCustom = QtWidgets.QAction(MainWindow)
        self.actionCustom.setObjectName("actionCustom")
        self.actionOnly_Selected_Files = QtWidgets.QAction(MainWindow)
        self.actionOnly_Selected_Files.setObjectName("actionOnly_Selected_Files")
        self.actionName = QtWidgets.QAction(MainWindow)
        self.actionName.setObjectName("actionName")
        self.actionExtension = QtWidgets.QAction(MainWindow)
        self.actionExtension.setObjectName("actionExtension")
        self.actionTime = QtWidgets.QAction(MainWindow)
        self.actionTime.setObjectName("actionTime")
        self.actionSize = QtWidgets.QAction(MainWindow)
        self.actionSize.setObjectName("actionSize")
        self.actionUnsorted = QtWidgets.QAction(MainWindow)
        self.actionUnsorted.setObjectName("actionUnsorted")
        self.actionButton_Bar = QtWidgets.QAction(MainWindow)
        self.actionButton_Bar.setObjectName("actionButton_Bar")
        self.actionButton_Bar2 = QtWidgets.QAction(MainWindow)
        self.actionButton_Bar2.setObjectName("actionButton_Bar2")
        self.actionChange_Settings_Files_Directly = QtWidgets.QAction(MainWindow)
        self.actionChange_Settings_Files_Directly.setObjectName("actionChange_Settings_Files_Directly")
        self.actionSave_Position = QtWidgets.QAction(MainWindow)
        self.actionSave_Position.setObjectName("actionSave_Position")
        self.actionSave_Settings = QtWidgets.QAction(MainWindow)
        self.actionSave_Settings.setObjectName("actionSave_Settings")
        self.actionChange_Start_Menu = QtWidgets.QAction(MainWindow)
        self.actionChange_Start_Menu.setObjectName("actionChange_Start_Menu")
        self.actionChange_Main_Menu = QtWidgets.QAction(MainWindow)
        self.actionChange_Main_Menu.setObjectName("actionChange_Main_Menu")
        self.menuPrint.addAction(self.actionFile_List)
        self.menuPrint.addAction(self.actionFile_list_with_subdirs)
        self.menuPrint.addAction(self.actionFile_contents)
        self.menuFile.addAction(self.actionChange_Attributes)
        self.menuFile.addAction(self.actionPack)
        self.menuFile.addAction(self.actionUnpack_Specific_Files)
        self.menuFile.addAction(self.actionTest_Archive_s)
        self.menuFile.addAction(self.actionCompare_by_Content)
        self.menuFile.addAction(self.actionAssociate_With)
        self.menuFile.addAction(self.actionInternal_Associations_pyCommander_only)
        self.menuFile.addAction(self.actionProperties)
        self.menuFile.addAction(self.actionCalculate_Occupied_Space)
        self.menuFile.addAction(self.actionMulti_Rename_Tool)
        self.menuFile.addAction(self.actionEdit_Comment)
        self.menuFile.addAction(self.menuPrint.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSplit_File)
        self.menuFile.addAction(self.actionCombine_File)
        self.menuFile.addAction(self.actionEncode_File)
        self.menuFile.addAction(self.actionDecode_File)
        self.menuFile.addAction(self.actionCreate_Checksum_File_s_CRC32_MD5_SHAT)
        self.menuFile.addAction(self.actionVerify_Checksum_from_checksum_files)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuMark.addAction(self.actionSelect_Group)
        self.menuMark.addAction(self.actionUnselect_Group)
        self.menuMark.addAction(self.actionSelect_All)
        self.menuMark.addAction(self.actionUnselect_All)
        self.menuMark.addAction(self.actionInvert_Selection)
        self.menuMark.addAction(self.actionSelect_All_With_Same_Extension)
        self.menuMark.addSeparator()
        self.menuMark.addAction(self.actionSave_Selection)
        self.menuMark.addAction(self.actionRestore_Selection)
        self.menuMark.addAction(self.actionSave_Selection_To_File)
        self.menuMark.addAction(self.actionLoad_Selection_From_File)
        self.menuMark.addSeparator()
        self.menuMark.addAction(self.actionCopy_Selected_Names_To_Clipboard)
        self.menuMark.addAction(self.actionCopy_Names_With_Path_To_Clipboard)
        self.menuMark.addAction(self.actionCopy_To_Clipboard_With_All_Details)
        self.menuMark.addAction(self.actionCopy_To_Clipboard_With_Path_Details)
        self.menuMark.addSeparator()
        self.menuMark.addAction(self.actionCompare_Directories)
        self.menuMark.addAction(self.actionMark_Newer_Hide_Same_Files)
        self.menuCommands.addAction(self.actionCD_Tree)
        self.menuCommands.addAction(self.actionSearch)
        self.menuCommands.addAction(self.actionSearch_in_separate_Process)
        self.menuCommands.addAction(self.actionVolume_Label)
        self.menuCommands.addAction(self.actionSystem_Information)
        self.menuCommands.addAction(self.actionSynchronize_Dirs)
        self.menuCommands.addAction(self.actionDirectory_Hotlist)
        self.menuCommands.addAction(self.actionGo_Back)
        self.menuCommands.addSeparator()
        self.menuCommands.addAction(self.actionOpen_command_prompt_window)
        self.menuCommands.addAction(self.actionBranch_View)
        self.menuCommands.addAction(self.actionOpen_Desktop_Folder)
        self.menuCommands.addAction(self.actionBackground_Transfer_Manager)
        self.menuCommands.addAction(self.actionSource_Target)
        self.menuCommands.addAction(self.actionTarget_Source)
        self.menuNet.addAction(self.actionNetwork_Connections)
        self.menuNet.addAction(self.actionDisconnect_Network_Drives)
        self.menuNet.addAction(self.actionShare_Current_Directory)
        self.menuNet.addAction(self.actionUnshare_Directory)
        self.menuNet.addAction(self.actionShow_Admin_Shares)
        self.menuNet.addSeparator()
        self.menuNet.addAction(self.actionFTP_Connect)
        self.menuNet.addAction(self.actionFTP_New_Connection)
        self.menuNet.addAction(self.actionFTP_Disconnect)
        self.menuNet.addAction(self.actionFTP_Show_Hidden_Files)
        self.menuNet.addAction(self.actionFTP_Download_From_List)
        self.menuNet.addAction(self.actionPORT_Connection_To_Other_PC)
        self.menuShow.addAction(self.actionBrief)
        self.menuShow.addAction(self.actionFull)
        self.menuShow.addAction(self.actionComments)
        self.menuShow.addAction(self.actionCustom_Columns_Mode)
        self.menuShow.addAction(self.actionCustom_View_Modes)
        self.menuShow.addAction(self.actionTree)
        self.menuShow.addAction(self.actionSeparate_Tree)
        self.menuShow.addAction(self.actionThumbnail_View)
        self.menuShow.addAction(self.actionQuick_View_Panel)
        self.menuShow.addAction(self.actionVertical_Arrangement)
        self.menuShow.addAction(self.actionNew_Folder_Tab)
        self.menuShow.addSeparator()
        self.menuShow.addAction(self.actionAll_Files)
        self.menuShow.addAction(self.actionPrograms)
        self.menuShow.addAction(self.action_3)
        self.menuShow.addAction(self.actionCustom)
        self.menuShow.addAction(self.actionOnly_Selected_Files)
        self.menuShow.addSeparator()
        self.menuShow.addAction(self.actionName)
        self.menuShow.addAction(self.actionExtension)
        self.menuShow.addAction(self.actionTime)
        self.menuShow.addAction(self.actionSize)
        self.menuShow.addAction(self.actionUnsorted)
        self.menuShow.addSeparator()
        self.menuonfiguration.addAction(self.actionButton_Bar)
        self.menuonfiguration.addAction(self.actionButton_Bar2)
        self.menuonfiguration.addAction(self.actionChange_Settings_Files_Directly)
        self.menuonfiguration.addAction(self.actionSave_Position)
        self.menuonfiguration.addAction(self.actionSave_Settings)
        self.menuStart.addAction(self.actionChange_Start_Menu)
        self.menuStart.addAction(self.actionChange_Main_Menu)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuMark.menuAction())
        self.menubar.addAction(self.menuCommands.menuAction())
        self.menubar.addAction(self.menuNet.menuAction())
        self.menubar.addAction(self.menuShow.menuAction())
        self.menubar.addAction(self.menuonfiguration.menuAction())
        self.menubar.addAction(self.menuStart.menuAction())
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Tab 1"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Tab 2"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "F3 View"))
        self.pushButton_2.setText(_translate("MainWindow", "F4 Edit "))
        self.pushButton_3.setText(_translate("MainWindow", "F5 Copy"))
        self.pushButton_4.setText(_translate("MainWindow", "F6 Move"))
        self.pushButton_5.setText(_translate("MainWindow", "F7 New Folder"))
        self.pushButton_6.setText(_translate("MainWindow", "F8 Delete"))
        self.pushButton_7.setText(_translate("MainWindow", "Alt+F4 Exit"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuPrint.setTitle(_translate("MainWindow", "Print"))
        self.menuMark.setTitle(_translate("MainWindow", "Mark"))
        self.menuCommands.setTitle(_translate("MainWindow", "Commands"))
        self.menuNet.setTitle(_translate("MainWindow", "Net"))
        self.menuShow.setTitle(_translate("MainWindow", "Show"))
        self.menuonfiguration.setTitle(_translate("MainWindow", "Configuration"))
        self.menuStart.setTitle(_translate("MainWindow", "Start"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionChange_Attributes.setText(_translate("MainWindow", "Change Attributes"))
        self.actionPack.setText(_translate("MainWindow", "Pack"))
        self.actionUnpack_Specific_Files.setText(_translate("MainWindow", "Unpack Specific Files"))
        self.actionTest_Archive_s.setText(_translate("MainWindow", "Test Archive(s)"))
        self.actionCompare_by_Content.setText(_translate("MainWindow", "Compare by Content"))
        self.actionAssociate_With.setText(_translate("MainWindow", "Associate With..."))
        self.actionInternal_Associations_pyCommander_only.setText(_translate("MainWindow", "Internal Associations (pyCommander only)"))
        self.actionProperties.setText(_translate("MainWindow", "Properties"))
        self.actionCalculate_Occupied_Space.setText(_translate("MainWindow", "Calculate Occupied Space..."))
        self.actionMulti_Rename_Tool.setText(_translate("MainWindow", "Multi-Rename Tool..."))
        self.actionEdit_Comment.setText(_translate("MainWindow", "Edit Comment..."))
        self.actionFile_List.setText(_translate("MainWindow", "File List"))
        self.actionFile_list_with_subdirs.setText(_translate("MainWindow", "File list with subdirs..."))
        self.actionFile_contents.setText(_translate("MainWindow", "File contents"))
        self.actionSplit_File.setText(_translate("MainWindow", "Split File ..."))
        self.actionCombine_File.setText(_translate("MainWindow", "Combine File..."))
        self.actionEncode_File.setText(_translate("MainWindow", "Encode File (MIME,UUE,XXE)..."))
        self.actionDecode_File.setText(_translate("MainWindow", "Decode File(MIME,UUE,XXE,BinHex)..."))
        self.actionCreate_Checksum_File_s_CRC32_MD5_SHAT.setText(_translate("MainWindow", "Create Checksum File(s) (CRC32,MD5,SHAT)..."))
        self.actionVerify_Checksum_from_checksum_files.setText(_translate("MainWindow", "Verify Checksum (from checksum files)"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionSelect_Group.setText(_translate("MainWindow", "Select Group..."))
        self.actionUnselect_Group.setText(_translate("MainWindow", "Unselect Group..."))
        self.actionSelect_All.setText(_translate("MainWindow", "Select All"))
        self.actionUnselect_All.setText(_translate("MainWindow", "Unselect All"))
        self.actionInvert_Selection.setText(_translate("MainWindow", "Invert Selection"))
        self.actionSelect_All_With_Same_Extension.setText(_translate("MainWindow", "Select All With Same Extension"))
        self.actionSave_Selection.setText(_translate("MainWindow", "Save Selection"))
        self.actionRestore_Selection.setText(_translate("MainWindow", "Restore Selection"))
        self.actionSave_Selection_To_File.setText(_translate("MainWindow", "Save Selection To File"))
        self.actionLoad_Selection_From_File.setText(_translate("MainWindow", "Load Selection From File"))
        self.actionCopy_Selected_Names_To_Clipboard.setText(_translate("MainWindow", "Copy Selected Names To Clipboard"))
        self.actionCopy_Names_With_Path_To_Clipboard.setText(_translate("MainWindow", "Copy Names With Path To Clipboard"))
        self.actionCopy_To_Clipboard_With_All_Details.setText(_translate("MainWindow", "Copy To Clipboard With All Details"))
        self.actionCopy_To_Clipboard_With_Path_Details.setText(_translate("MainWindow", "Copy To Clipboard With Path + Details"))
        self.actionCompare_Directories.setText(_translate("MainWindow", "Compare Directories"))
        self.actionMark_Newer_Hide_Same_Files.setText(_translate("MainWindow", "Mark Newer, Hide Same Files"))
        self.actionCD_Tree.setText(_translate("MainWindow", "CD Tree"))
        self.actionSearch.setText(_translate("MainWindow", "Search"))
        self.actionSearch_in_separate_Process.setText(_translate("MainWindow", "Search in separate Process"))
        self.actionVolume_Label.setText(_translate("MainWindow", "Volume Label..."))
        self.actionSystem_Information.setText(_translate("MainWindow", "System Information..."))
        self.actionSynchronize_Dirs.setText(_translate("MainWindow", "Synchronize Dirs..."))
        self.actionDirectory_Hotlist.setText(_translate("MainWindow", "Directory Hotlist"))
        self.actionGo_Back.setText(_translate("MainWindow", "Go Back"))
        self.actionOpen_command_prompt_window.setText(_translate("MainWindow", "Open command prompt window"))
        self.actionBranch_View.setText(_translate("MainWindow", "Branch View"))
        self.actionOpen_Desktop_Folder.setText(_translate("MainWindow", "Open Desktop Folder"))
        self.actionBackground_Transfer_Manager.setText(_translate("MainWindow", "Background Transfer Manager..."))
        self.actionSource_Target.setText(_translate("MainWindow", "Source<->Target"))
        self.actionTarget_Source.setText(_translate("MainWindow", "Target<->Source"))
        self.actionNetwork_Connections.setText(_translate("MainWindow", "Network Connections..."))
        self.actionDisconnect_Network_Drives.setText(_translate("MainWindow", "Disconnect Network Drives..."))
        self.actionShare_Current_Directory.setText(_translate("MainWindow", "Share Current Directory..."))
        self.actionUnshare_Directory.setText(_translate("MainWindow", "Unshare Directory..."))
        self.actionShow_Admin_Shares.setText(_translate("MainWindow", "Show Admin Shares"))
        self.actionFTP_Connect.setText(_translate("MainWindow", "FTP Connect..."))
        self.actionFTP_New_Connection.setText(_translate("MainWindow", "FTP New Connection..."))
        self.actionFTP_Disconnect.setText(_translate("MainWindow", "FTP Disconnect"))
        self.actionFTP_Show_Hidden_Files.setText(_translate("MainWindow", "FTP Show Hidden Files"))
        self.actionFTP_Download_From_List.setText(_translate("MainWindow", "FTP Download From List..."))
        self.actionPORT_Connection_To_Other_PC.setText(_translate("MainWindow", "PORT Connection To Other PC"))
        self.actionBrief.setText(_translate("MainWindow", "Brief"))
        self.actionFull.setText(_translate("MainWindow", "Full"))
        self.actionComments.setText(_translate("MainWindow", "Comments"))
        self.actionCustom_Columns_Mode.setText(_translate("MainWindow", "Custom Columns Mode"))
        self.actionCustom_View_Modes.setText(_translate("MainWindow", "Custom View Modes"))
        self.actionTree.setText(_translate("MainWindow", "Tree"))
        self.actionSeparate_Tree.setText(_translate("MainWindow", "Separate Tree"))
        self.actionThumbnail_View.setText(_translate("MainWindow", "Thumbnail View"))
        self.actionQuick_View_Panel.setText(_translate("MainWindow", "Quick View Panel"))
        self.actionVertical_Arrangement.setText(_translate("MainWindow", "Vertical Arrangement"))
        self.actionNew_Folder_Tab.setText(_translate("MainWindow", "New Folder Tab"))
        self.actionAll_Files.setText(_translate("MainWindow", "All Files"))
        self.actionPrograms.setText(_translate("MainWindow", "Programs"))
        self.action_3.setText(_translate("MainWindow", "*.*"))
        self.actionCustom.setText(_translate("MainWindow", "Custom..."))
        self.actionOnly_Selected_Files.setText(_translate("MainWindow", "Only Selected Files"))
        self.actionName.setText(_translate("MainWindow", "Name"))
        self.actionExtension.setText(_translate("MainWindow", "Extension"))
        self.actionTime.setText(_translate("MainWindow", "Time"))
        self.actionSize.setText(_translate("MainWindow", "Size"))
        self.actionUnsorted.setText(_translate("MainWindow", "Unsorted"))
        self.actionButton_Bar.setText(_translate("MainWindow", "Button Bar"))
        self.actionButton_Bar2.setText(_translate("MainWindow", "Button Bar2(Vertical)"))
        self.actionChange_Settings_Files_Directly.setText(_translate("MainWindow", "Change Settings Files Directly"))
        self.actionSave_Position.setText(_translate("MainWindow", "Save Position"))
        self.actionSave_Settings.setText(_translate("MainWindow", "Save Settings"))
        self.actionChange_Start_Menu.setText(_translate("MainWindow", "Change Start Menu"))
        self.actionChange_Main_Menu.setText(_translate("MainWindow", "Change Main Menu"))
