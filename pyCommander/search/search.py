# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtGui, QtCore
from ui_search import Ui_MainWindow

class SearchWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.checkBoxOpenedTabs.toggled.connect(self.checkbox_opened_tabs_toggled)
        self.checkBoxSelectedDirectoriesAndFiles.toggled.connect(self.checkbox_opened_tabs_toggled)
        self.comboBoxEncoding.currentIndexChanged.connect(self.combobox_index_changed)
        self.comboBoxEncoding.currentTextChanged.connect(self.combobox_text_changed)
        
        self.pushButtonStart.clicked.connect(self.button_start_clicked)
        
    def connectSignalsSlots(self):        
        self.actionNewSearch.triggered.connect(self.new_search)       
        self.actionNewSearchClearFilters.triggered.connect(self.new_search_clear_filters)       
        self.actionLastSearch.triggered.connect(self.last_search)         
        self.actionStart.triggered.connect(self.start)    
        self.actionCancel.triggered.connect(self.cancel)         
        self.actionClose.triggered.connect(self.close)         
        self.actionCancelSearchAndCloseWindow.triggered.connect(self.cancel_search_close_window)         
        self.actionCancelSearchCloseAndFreeFromMemory.triggered.connect(self.cancel_search_close_free_memory)         
        self.actionForAllOthersCancelCloseAndFreeFromMemory.triggered.connect(self.all_others_cancel_close_free_memory)         
        self.actionForAllSearchesCancelCloseAndFreeMemory.triggered.connect(self.all_searches_cancel_close_free_memory)         
        self.actionGoToPageStandard.triggered.connect(self.goto_page_standard)         
        self.actionGoToPageAdvanced.triggered.connect(self.goto_page_advanced)         
        self.actionGoToPagePlugins.triggered.connect(self.goto_page_plugins)         
        self.actionGoToPageLoadSave.triggered.connect(self.goto_page_loadsave)        
        self.actionGoToPageResults.triggered.connect(self.goto_page_results)        
        self.actionNewSearchInstance.triggered.connect(self.new_search_instance)         
        self.actionViewCurrentSearchInstances.triggered.connect(self.current_search_instance)         
        self.actionView.triggered.connect(self.view)         
        self.actionEdit.triggered.connect(self.edit)         
        self.actionFeedToListbox.triggered.connect(self.feed_to_listbox)         
        self.actionGoToFile.triggered.connect(self.goto_file)         
        self.actionConfigurationOfSearches.triggered.connect(self.configuration_searches)         
        self.actionConfigurationOfHotKeys.triggered.connect(self.configuration_hot_keys) 
        
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
     
    def button_start_clicked(self, button):
        print("The button was pressed!")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    window = SearchWindow()
    window.show()
    sys.exit(app.exec_())