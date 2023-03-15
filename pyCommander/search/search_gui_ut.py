# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 09:44:03 2023

@author: Yevhen_Vieskov
"""

#https://doc.qt.io/qtforpython/overviews/qttestlib-tutorial1-example.html
#https://stackoverflow.com/questions/34045246/unittesting-pyqt-app
#https://stackoverflow.com/questions/1616228/pyqt-gui-testing
#https://johnnado.com/pyqt-qtest-example/          !!!!!!!
#https://doc.qt.io/qtforpython/overviews/qtest-overview.html
#https://github.com/jmcgeheeiv/pyqttestexample
#https://github.com/biolab/PyQtTester
#https://sharplydescribed.wordpress.com/2020/09/17/gui-qt5-testing-with-python-qsignalspy-qtest/  !!!!!

#https://stackoverflow.com/questions/61213729/simulate-the-click-on-a-button-in-the-pyqt5-qmessagebox-widget-during-unittest
#https://stackoverflow.com/questions/55064026/pyqt-unit-test-that-qdialog-is-created
#https://stackoverflow.com/questions/67467649/python-unittest-verify-button-clicked
#https://stackoverflow.com/questions/67467649/python-unittest-verify-button-clicked
#https://stackoverflow.com/questions/72469068/how-to-test-that-a-pyqt-button-signal-calls-a-function
#https://stackoverflow.com/questions/59147908/how-to-click-on-qmessagebox-with-pytest-qt



import sys
from unittest import TestCase
from unittest.mock import patch as patch

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtTest import QTest, QSignalSpy
from PyQt5.QtCore import Qt
import search
#import ui_search.py



 
class SearchWidgetTest(TestCase):
    @classmethod         
    def setUp(self):
        #self.w = search.SearchWindow()
        self.ctx = QApplication([])
      
    def test_on_click(self):
        with patch('pushButtonStart.on_click') as clickCheck:
            app = search.SearchWindow()
            QTest.mouseClick(app.pushButtonStart, Qt.LeftButton)
            self.assertTrue(clickCheck.called)
 
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













