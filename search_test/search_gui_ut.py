# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 09:44:03 2023

@author: Yevhen_Vieskov
"""

# https://doc.qt.io/qtforpython/overviews/qttestlib-tutorial1-example.html
# https://stackoverflow.com/questions/34045246/unittesting-pyqt-app
# https://stackoverflow.com/questions/1616228/pyqt-gui-testing
# https://johnnado.com/pyqt-qtest-example/          !!!!!!!
# https://doc.qt.io/qtforpython/overviews/qtest-overview.html
# https://github.com/jmcgeheeiv/pyqttestexample
# https://github.com/biolab/PyQtTester
# https://sharplydescribed.wordpress.com/2020/09/17/gui-qt5-testing-with-python-qsignalspy-qtest/  !!!!!

# https://stackoverflow.com/questions/61213729/simulate-the-click-on-a-button-in-the-pyqt5-qmessagebox-widget-during-unittest
# https://stackoverflow.com/questions/55064026/pyqt-unit-test-that-qdialog-is-created
# https://stackoverflow.com/questions/67467649/python-unittest-verify-button-clicked
# https://stackoverflow.com/questions/67467649/python-unittest-verify-button-clicked
# https://stackoverflow.com/questions/72469068/how-to-test-that-a-pyqt-button-signal-calls-a-function
# https://stackoverflow.com/questions/59147908/how-to-click-on-qmessagebox-with-pytest-qt
# https://pyqt.riverbankcomputing.narkive.com/9C5Xbq8M/here-is-how-to-write-gui-unit-tests-with-qttest-and-unittest
# https://stackoverflow.com/questions/67990408/qttest-under-pyqt5-fails-when-widgets-under-test-have-to-be-visible-to-work
#https://stackoverflow.com/questions/61044136/modulenotfounderror-when-trying-to-use-mock-patch-on-a-method


import os
import sys
import unittest
from unittest.mock import patch as patch

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtTest import QTest, QSignalSpy
from PyQt5.QtCore import Qt
#import search_files.search as search
from search_files.search import SearchWindow


#sys.path
#sys.path.append('C:/Users/Yevhen_Vieskov/pyCommander/search_files/search.py')

#path = 'C:/Users/Yevhen_Vieskov/pyCommander/search_files/search.py'
#os.environ['PATH'] += ':'+path



class SearchWidgetTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        '''Create the GUI'''
        self.form = SearchWindow()
        # self.w.show()
        #self.ctx = QApplication([])
        
    def create_form(self):
        self.setUp()
        

    def test_pb_start_on_click(self):      
        with patch('search_files.search.SearchWindow.button_start_clicked') as fake_on_click:
            app =  SearchWindow()            
            QTest.mouseClick(app.pushButtonStart, Qt.LeftButton)
            self.assertTrue(fake_on_click.called)
            
            
    def test_pb_cancel_on_click(self):      
        with patch('search_files.search.SearchWindow.button_cancel_clicked') as fake_on_click:
            app =  SearchWindow()            
            QTest.mouseClick(app.pushButtonCancel, Qt.LeftButton)
            self.assertTrue(fake_on_click.called)
            
    def test_pb_close_on_click(self):      
        with patch('search_files.search.SearchWindow.button_close_clicked') as fake_on_click:
            app =  SearchWindow()            
            QTest.mouseClick(app.pushButtonClose, Qt.LeftButton)
            self.assertTrue(fake_on_click.called)
           
    def test_pb_new_search_on_click(self):      
        with patch('search_files.search.SearchWindow.button_new_search_clicked') as fake_on_click:
            app =  SearchWindow()            
            QTest.mouseClick(app.pushButtonNewSearch, Qt.LeftButton)
            self.assertTrue(fake_on_click.called)
            
    def test_pb_last_search_on_click(self):      
        with patch('search_files.search.SearchWindow.button_last_search_clicked') as fake_on_click:
            app =  SearchWindow()            
            QTest.mouseClick(app.pushButtonLastSearch, Qt.LeftButton)
            self.assertTrue(fake_on_click.called)
            
    def test_pb_file_open_on_click(self):      
        with patch('search_files.search.SearchWindow.button_file_open_clicked') as fake_on_click:
            app =  SearchWindow()            
            QTest.mouseClick(app.pushButtonFileOpen, Qt.LeftButton)
            self.assertTrue(fake_on_click.called)
            
    def test_pb_add_on_click(self):      
        with patch('search_files.search.SearchWindow.button_add_clicked') as fake_on_click:
            app =  SearchWindow()            
            QTest.mouseClick(app.pushButtonAdd, Qt.LeftButton)
            self.assertTrue(fake_on_click.called)
            
    def test_pb_help_on_click(self):      
        with patch('search_files.search.SearchWindow.button_help_clicked') as fake_on_click:
            app =  SearchWindow()            
            QTest.mouseClick(app.pushButtonHelp, Qt.LeftButton)
            self.assertTrue(fake_on_click.called)
            
    def test_pb_more_rules_on_click(self):      
        with patch('search_files.search.SearchWindow.button_more_rules_clicked') as fake_on_click:
            app =  SearchWindow()            
            QTest.mouseClick(app.pushButtonMoreRules, Qt.LeftButton)
            self.assertTrue(fake_on_click.called)
            
    def test_pb_less_rules_on_click(self):      
        with patch('search_files.search.SearchWindow.button_less_rules_clicked') as fake_on_click:
            app =  SearchWindow()            
            QTest.mouseClick(app.pushButtonLessRules, Qt.LeftButton)
            self.assertTrue(fake_on_click.called)
            
    def test_pb_load_on_click(self):      
        with patch('search_files.search.SearchWindow.button_load_clicked') as fake_on_click:
            app =  SearchWindow()            
            QTest.mouseClick(app.pushButtonLoad, Qt.LeftButton)
            self.assertTrue(fake_on_click.called)
            
            
    def test_pb_save_on_click(self):      
        with patch('search_files.search.SearchWindow.button_save_clicked') as fake_on_click:
            app =  SearchWindow()            
            QTest.mouseClick(app.pushButtonSave, Qt.LeftButton)
            self.assertTrue(fake_on_click.called)
            
    def test_pb_delete_on_click(self):      
        with patch('search_files.search.SearchWindow.button_delete_clicked') as fake_on_click:
            app =  SearchWindow()            
            QTest.mouseClick(app.pushButtonDelete, Qt.LeftButton)
            self.assertTrue(fake_on_click.called)
           
      
              
    '''def test_pb_view_on_click(self):      
        with patch('search_files.search.SearchWindow.button_view_clicked') as fake_on_click:
            app =  SearchWindow()            
            QTest.mouseClick(app.pushButtonView, Qt.LeftButton)
            self.assertTrue(fake_on_click.called)
         
    def test_pb_edit_on_click(self):      
        with patch('search_files.search.SearchWindow.button_edit_clicked') as fake_on_click:
            app =  SearchWindow()            
            QTest.mouseClick(app.pushButtonEdit, Qt.LeftButton)
            self.assertTrue(fake_on_click.called)
          
    def test_pb_load_on_click(self):      
        with patch('search_files.search.SearchWindow.button_goto_file_clicked') as fake_on_click:
            app =  SearchWindow()            
            QTest.mouseClick(app.pushButtonGoToFile, Qt.LeftButton)
            self.assertTrue(fake_on_click.called)
           
    def test_pb_feed_to_listbox_on_click(self):      
        with patch('search_files.search.SearchWindow.button_feed_to_listbox_clicked') as fake_on_click:
            app =  SearchWindow()            
            QTest.mouseClick(app.pushButtonFeedToListbox, Qt.LeftButton)
            self.assertTrue(fake_on_click.called)'''
            
          
   
    def test_buttons(self):
        self.form.pushButtonStart.click()
        self.assertEqual(self.form.pushButtonStart.text(), "Start")
        self.form.pushButtonCancel.click()
        self.assertEqual(self.form.pushButtonCancel.text(), "Cancel")
        self.form.pushButtonClose.click()
        self.assertEqual(self.form.pushButtonClose.text(), "Close")
        self.form.pushButtonNewSearch.click()
        self.assertEqual(self.form.pushButtonNewSearch.text(), "New search")
        self.form.pushButtonLastSearch.click()
        self.assertEqual(self.form.pushButtonLastSearch.text(), "Last search")
        self.form.pushButtonFileOpen.click()
        self.assertEqual(self.form.pushButtonFileOpen.text(), "Open")
        self.form.pushButtonAdd.click()        
        self.assertEqual(self.form.pushButtonAdd.text(), "Add")
        self.form.pushButtonHelp.click()
        self.assertEqual(self.form.pushButtonHelp.text(), "Help")
        self.form.pushButtonMoreRules.click()
        self.assertEqual(self.form.pushButtonMoreRules.text(), "More rules")
        self.form.pushButtonLessRules.click()
        self.assertEqual(self.form.pushButtonLessRules.text(), "Less rules")
        self.form.pushButtonLoad.click()
        self.assertEqual(self.form.pushButtonLoad.text(), "Load")
        self.form.pushButtonSave.click()
        self.assertEqual(self.form.pushButtonSave.text(), "Save")
        self.form.pushButtonDelete.click()
        self.assertEqual(self.form.pushButtonDelete.text(), "Delete")
        self.form.pushButtonView.click()
        self.assertEqual(self.form.pushButtonView.text(), "View")
        self.form.pushButtonEdit.click()
        self.assertEqual(self.form.pushButtonEdit.text(), "Edit")
        self.form.pushButtonGoToFile.click()
        self.assertEqual(self.form.pushButtonGoToFile.text(), "Go to file")
        self.form.pushButtonFeedToListbox.click()
        self.assertEqual(self.form.pushButtonFeedToListbox.text(), "Feed to listbox")
        
        
        
'''
    def test_PushButton(self):
        (self.ui.pushButtonStart.clicked.connect(self.button_start_clicked))
        self.assertEqual(self.ui.bloodTextEdit.placeholderText(), "")
        self.assertEqual(self.ui.renalTextEdit.placeholderText(), "")
        self.assertEqual(self.ui.liverTextEdit.placeholderText(), "")
        self.assertEqual(self.ui.thyroidTextEdit.placeholderText(), "")
        self.assertEqual(self.ui.electrolyteTextEdit.placeholderText(), "")
        self.assertEqual(self.ui.lipidTextEdit.placeholderText(), "")

'''


# ==============================================================================
if __name__ == '__main__':
    # Must construct a QApplication before a QWidget
    ctx = QApplication(sys.argv)
    unittest.main()
    #mainw = SearchWidgetTest()
    # app.setActiveWindow(mainw)
    # mainw.show()
