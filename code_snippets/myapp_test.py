# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 22:22:53 2023

@author: Yevhen_Vieskov
"""
#https://stackoverflow.com/questions/67345474/extend-generated-testapp-to-verify-pyqt5-button-click
from unittest import mock, TestCase
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
import unittest
from myapp import App


class TestApp(TestCase):

    def setUp(self):
        #self.ctx = QApplication([])
        #app = App()
        pass

    def test_on_click(self):
        self.setUp()
        with mock.patch("myapp.App.on_click") as fake_on_click:
            app = App()
            QTest.mouseClick(app.button, Qt.LeftButton)
            self.assertTrue(fake_on_click.called)
            
            
            
            
if __name__ == '__main__':
    # Must construct a QApplication before a QWidget
    ctx = QApplication([])
    unittest.main()        