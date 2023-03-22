# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import pyqtSlot
from ui_search import Ui_MainWindow
#https://stackoverflow.com/questions/16981921/relative-imports-in-python-3

class SearchWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        
        self.checkBoxOpenedTabs.toggled.connect(
            self.checkbox_opened_tabs_toggled)
        self.checkBoxSelectedDirectoriesAndFiles.toggled.connect(
            self.checkbox_selected_directory_and_files_toggled)
        self.checkBoxFollowSymlinks.toggled.connect(
            self.checkbox_follow_symlinks_toggled)
        self.checkBoxSearchInArchives.toggled.connect(
            self.checkbox_search_in_archives_toggled)
        self.checkBoxSearchForPartOfFileName.toggled.connect(
            self.checkbox_search_for_part_of_file_name_toggled)
        self.checkBoxRegularExpression.toggled.connect(
            self.checkbox_regular_expression_toggled)
        self.checkBoxFindTextInFile.toggled.connect(
            self.checkbox_find_text_in_file_toggled)
        self.checkBoxReplaceBy.toggled.connect(
            self.checkbox_replace_by_toggled)
        self.checkBoxFindFilesNotContainingText.toggled.connect(
            self.checkbox_find_files_not_containing_text_toggled)
        self.checkBoxCaseSensitive.toggled.connect(
            self.checkbox_case_sensitive_toggled)
        self.checkBoxRegularExpressionFindData.toggled.connect(
            self.checkbox_regular_expression_find_data_toggled)
        self.checkBoxOfficeXML.toggled.connect(
            self.checkbox_office_xml_toggled)
        self.checkBoxHexadecimal.toggled.connect(
            self.checkbox_hexadecimal_toggled)
        self.checkBoxNotOlderThan.toggled.connect(
            self.checkbox_not_older_than_toggled)
        self.checkBoxSizeFrom.toggled.connect(
            self.checkbox_size_from_toggled)
        self.checkBoxSizeTo.toggled.connect(
            self.checkbox_size_to_toggled)
        self.checkBoxDateFrom.toggled.connect(
            self.checkbox_date_from_toggled)
        self.checkBoxDateTo.toggled.connect(
            self.checkbox_date_to_toggled)
        self.checkBoxTimeFrom.toggled.connect(
            self.checkbox_time_from_toggled)
        self.checkBoxTimeTo.toggled.connect(
            self.checkbox_time_to_toggled)
        self.checkBoxFindDuplicateFiles.toggled.connect(
            self.checkbox_find_duplicate_files_toggled)
        self.checkBoxSameName.toggled.connect(
            self.checkbox_same_name_toggled)
        self.checkBoxSameSize.toggled.connect(
            self.checkbox_same_size_toggled)
        self.checkBoxSameHash.toggled.connect(
            self.checkbox_same_hash_toggled)        
        self.checkBoxSomeContent.toggled.connect(
            self.checkbox_some_content_toggled)
        self.checkBoxUseSearchPlugin.toggled.connect(
            self.checkbox_use_search_plugin_toggled)
        self.checkBoxUseContentPlugin.toggled.connect(
            self.checkbox_content_plugin_toggled)      
        
        '''self.comboBoxExcludeSubdirectories
        self.comboBoxExcludeSubdirectories
        self.comboBoxSearchSubdirectories
        self.comboBoxSearchSubdirectories
        self.comboBoxExcludeFiles
        self.comboBoxExcludeFiles
        self.comboBoxEncoding.currentIndexChanged.connect(
            self.combobox_index_changed)
        self.comboBoxEncoding.currentTextChanged.connect(
            self.combobox_text_changed)
        self.comboBoxNotOlderThan
        self.comboBoxNotOlderThan
        self.comboBoxSizeTo
        self.comboBoxSizeTo'''
        
        #self.lineEditStartInDirectory.text()
        #e2 = QLineEdit()
        #e2.setValidator(QDoubleValidator(0.99,99.99,2))
        #e3 = QLineEdit()
        #e3.setInputMask("+99_9999_999999")

        #self.lineEditFileMask
        #self.lineEditFindTextInFile
        #self.lineEditReplaceBy
        #self.lineEditAttributes
        
        '''self.spinBoxNotOlderThan
        
        self.doubleSpinBoxSizeFrom
        self.doubleSpinBoxSizeTo
        
        self.dateEditFrom
        self.dateEditDateTo
        
        self.timeEditTimeFrom
        self.timeEditTimeTo'''
        
        #QDoubleValidator, QIntValidator, QRegExpValidator,
        
        #qlabel.setText(text)

        self.pushButtonStart.clicked.connect(self.button_start_clicked)
        self.pushButtonCancel.clicked.connect(self.button_cancel_clicked)
        self.pushButtonClose.clicked.connect(self.button_close_clicked)
        self.pushButtonNewSearch.clicked.connect(self.button_new_search_clicked)
        self.pushButtonLastSearch.clicked.connect(self.button_last_search_clicked)
        self.pushButtonAdd.clicked.connect(self.button_add_clicked)
        self.pushButtonHelp.clicked.connect(self.button_help_clicked)
        self.pushButtonMoreRules.clicked.connect(self.button_more_rules_clicked)
        self.pushButtonLessRules.clicked.connect(self.button_less_rules_clicked)
        self.pushButtonLoad.clicked.connect(self.button_load_clicked)
        self.pushButtonSave.clicked.connect(self.button_save_clicked)
        self.pushButtonSaveWithStartInDirectory.clicked.connect(self.button_save_with_start_in_directory_clicked)
        self.pushButtonDelete.clicked.connect(self.button_delete_clicked)
        self.pushButtonFileOpen.clicked.connect(self.button_file_open_clicked)
    
    
    

    def connectSignalsSlots(self):
        self.actionNewSearch.triggered.connect(self.new_search)
        self.actionNewSearchClearFilters.triggered.connect(
            self.new_search_clear_filters)
        self.actionLastSearch.triggered.connect(self.last_search)
        self.actionStart.triggered.connect(self.start)
        self.actionCancel.triggered.connect(self.cancel)
        self.actionClose.triggered.connect(self.close)
        self.actionCancelSearchAndCloseWindow.triggered.connect(
            self.cancel_search_close_window)
        self.actionCancelSearchCloseAndFreeFromMemory.triggered.connect(
            self.cancel_search_close_free_memory)
        self.actionForAllOthersCancelCloseAndFreeFromMemory.triggered.connect(
            self.all_others_cancel_close_free_memory)
        self.actionForAllSearchesCancelCloseAndFreeMemory.triggered.connect(
            self.all_searches_cancel_close_free_memory)
        self.actionGoToPageStandard.triggered.connect(self.goto_page_standard)
        self.actionGoToPageAdvanced.triggered.connect(self.goto_page_advanced)
        self.actionGoToPagePlugins.triggered.connect(self.goto_page_plugins)
        self.actionGoToPageLoadSave.triggered.connect(self.goto_page_loadsave)
        self.actionGoToPageResults.triggered.connect(self.goto_page_results)
        self.actionNewSearchInstance.triggered.connect(
            self.new_search_instance)
        self.actionViewCurrentSearchInstances.triggered.connect(
            self.current_search_instance)
        self.actionView.triggered.connect(self.view)
        self.actionEdit.triggered.connect(self.edit)
        self.actionFeedToListbox.triggered.connect(self.feed_to_listbox)
        self.actionGoToFile.triggered.connect(self.goto_file)
        self.actionConfigurationOfSearches.triggered.connect(
            self.configuration_searches)
        self.actionConfigurationOfHotKeys.triggered.connect(
            self.configuration_hot_keys)

    def new_search():
        pass

    def new_search_clear_filters():
        pass

    def last_search():
        pass

    def start():
        pass

    def cancel():
        pass

    def close():
        pass

    def cancel_search_close_window():
        pass

    def cancel_search_close_free_memory():
        pass

    def all_others_cancel_close_free_memory():
        pass

    def all_searches_cancel_close_free_memory():
        pass

    def goto_page_standard():
        pass

    def goto_page_advanced():
        pass

    def goto_page_plugins():
        pass

    def goto_page_loadsave():
        pass

    def goto_page_results():
        pass

    def new_search_instance():
        pass

    def current_search_instance():
        pass

    def view():
        pass

    def edit():
        pass

    def feed_to_listbox():
        pass

    def goto_file():
        pass

    def configuration_searches():
        pass

    def configuration_hot_keys():
        pass

    def checkbox_opened_tabs_toggled(self):

        selected = []

        if self.checkBoxOpenedTabs.isChecked():
            selected.append("Kestrel")

        if self.checkBoxSelectedDirectoriesAndFiles.isChecked():
            selected.append("Sparrowhawk")

    def combobox_encoding_changed(self):
        text = self.ui.comboBoxEncoding.currentText()
        print(text)

    def combobox_index_changed(self, i):
        print(i)

    def combobox_text_changed(self, s):
        print(s)
    
    @pyqtSlot()
    def button_start_clicked(self):
        print("The button was pressed!")
        
    @pyqtSlot()    
    def button_cancel_clicked(self):
        pass
    
    @pyqtSlot()
    def button_close_clicked(self):
        pass
    
    @pyqtSlot()
    def button_new_search_clicked(self):
        pass
    
    @pyqtSlot()
    def button_last_search_clicked(self):
        pass
    
    @pyqtSlot()
    def button_add_clicked(self):
        pass
    
    @pyqtSlot()
    def button_help_clicked(self):
        pass
    
    @pyqtSlot()
    def button_more_rules_clicked(self):
        pass
    
    @pyqtSlot()
    def button_less_rules_clicked(self):
        pass
    
    @pyqtSlot()
    def button_load_clicked(self):
        pass
    
    @pyqtSlot()
    def button_save_clicked(self):
        pass
    
    @pyqtSlot()
    def button_save_with_start_in_directory_clicked(self):
        pass
    
    @pyqtSlot()
    def button_delete_clicked(self):
        pass     
    
    @pyqtSlot()    
    def button_file_open_clicked(self):
        pass
    
    @pyqtSlot()    
    def button_view_clicked(self):
        pass
       
    @pyqtSlot()    
    def button_edit_clicked(self):
        pass
    
    @pyqtSlot()    
    def button_goto_file_clicked(self):
        pass
    
    @pyqtSlot()    
    def button_feed_to_listbox_clicked(self):
        pass
    
    def checkbox_opened_tabs_toggled(self):
        pass

    def checkbox_selected_directory_and_files_toggled(self):
        pass

    def checkbox_follow_symlinks_toggled(self):
        pass

    def checkbox_search_in_archives_toggled(self):
        pass

    def checkbox_search_for_part_of_file_name_toggled(self):
        pass

    def checkbox_regular_expression_toggled(self):
        pass

    def checkbox_find_text_in_file_toggled(self):
        pass

    def checkbox_replace_by_toggled(self):
        pass

    def checkbox_find_files_not_containing_text_toggled(self):
        pass

    def checkbox_case_sensitive_toggled(self):
        pass

    def checkbox_regular_expression_find_data_toggled(self):
        pass

    def checkbox_office_xml_toggled(self):
        pass

    def checkbox_hexadecimal_toggled(self):
        pass

    def checkbox_not_older_than_toggled(self):
        pass

    def checkbox_size_from_toggled(self):
        pass

    def checkbox_size_to_toggled(self):
        pass

    def checkbox_date_from_toggled(self):
        pass

    def checkbox_date_to_toggled(self):
        pass

    def checkbox_time_from_toggled(self):
        pass

    def checkbox_time_to_toggled(self):
        pass

    def checkbox_find_duplicate_files_toggled(self):
        pass

    def checkbox_same_name_toggled(self):
        pass

    def checkbox_same_size_toggled(self):
        pass

    def checkbox_same_hash_toggled(self):
        pass       

    def checkbox_some_content_toggled(self):
        pass

    def checkbox_use_search_plugin_toggled(self):
        pass

    def checkbox_content_plugin_toggled(self):
        pass
        
#mock functions for unit tests

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    window = SearchWindow()
    window.show()
    sys.exit(app.exec_())
