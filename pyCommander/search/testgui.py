# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 12:53:08 2023

@author: Yevhen_Vieskov
"""

import sys
 
sys.path.append("../ui") # to see modules in parent's directory
 
import unittest
from PyQt5.QtTest import QTest, QSignalSpy
from answer_ui import Ui_Answer
from PyQt5.QtWidgets import QWidget, QApplication
 
 
app = QApplication(sys.argv) # without it we cannot test anything
 
 
class AnswerWidgetTest(unittest.TestCase):
     
    answerWidget = None  # hold QWidget in variable  
    ui = None   # hold GUI in variable
     
    def setUp(self):
        self.answerWidget = QWidget() # create empty QWidget
        self.ui = Ui_Answer() # we want to test GUI - only
        self.ui.setupUi(self.answerWidget) # set GUI for freshly created QWidget
 
 
    def test_textEditsWidgetsText(self):
        self.assertEqual(self.ui.bloodTextEdit.placeholderText(), "")
        self.assertEqual(self.ui.renalTextEdit.placeholderText(), "")
        self.assertEqual(self.ui.liverTextEdit.placeholderText(), "")
        self.assertEqual(self.ui.thyroidTextEdit.placeholderText(), "")
        self.assertEqual(self.ui.electrolyteTextEdit.placeholderText(), "")
        self.assertEqual(self.ui.lipidTextEdit.placeholderText(), "")
 
         
    def test_textEditsWidgetsNotDisabled(self):
        self.assertTrue(self.ui.bloodTextEdit.isEnabled())
        self.assertTrue(self.ui.renalTextEdit.isEnabled())
        self.assertTrue(self.ui.liverTextEdit.isEnabled())
        self.assertTrue(self.ui.thyroidTextEdit.isEnabled())
        self.assertTrue(self.ui.electrolyteTextEdit.isEnabled())
        self.assertTrue(self.ui.lipidTextEdit.isEnabled())
 
         
    def test_textEditsReadOnly(self):
        self.assertTrue(self.ui.bloodTextEdit.isReadOnly())
        self.assertTrue(self.ui.renalTextEdit.isReadOnly())
        self.assertTrue(self.ui.liverTextEdit.isReadOnly())
        self.assertTrue(self.ui.thyroidTextEdit.isReadOnly())
        self.assertTrue(self.ui.electrolyteTextEdit.isReadOnly())
        self.assertTrue(self.ui.lipidTextEdit.isReadOnly())
         
        # try to type "example" into textEdit for blood tests
        QTest.keyClicks(self.ui.bloodTextEdit, "example")
         
        self.assertEqual(self.ui.bloodTextEdit.placeholderText(), "")
 
         
    def test_changedFontFamily(self):
        signalspy = QSignalSpy(self.ui.fontComboBox.currentIndexChanged) # monitors fontComboBox, when current index is changing
        self.ui.fontComboBox.setCurrentIndex(2)  # we change current index for fontComboBox 
         
        # current connections for a signal
        self.assertEqual(self.ui.fontComboBox.receivers(self.ui.fontComboBox.currentIndexChanged), 1)
         
        self.assertEqual(len(signalspy), 1)  # first call
        self.assertTrue(signalspy.isValid())
         
        self.assertEqual(self.ui.fontComboBox.currentText(), self.ui.bloodTextEdit.fontFamily())
        self.assertEqual(self.ui.fontComboBox.currentText(), self.ui.renalTextEdit.fontFamily())
        self.assertEqual(self.ui.fontComboBox.currentText(), self.ui.liverTextEdit.fontFamily())
        self.assertEqual(self.ui.fontComboBox.currentText(), self.ui.thyroidTextEdit.fontFamily())
        self.assertEqual(self.ui.fontComboBox.currentText(), self.ui.electrolyteTextEdit.fontFamily())
        self.assertEqual(self.ui.fontComboBox.currentText(), self.ui.lipidTextEdit.fontFamily())
         
        self.ui.fontComboBox.setCurrentIndex(3) # we change current index again
         
        self.assertTrue(signalspy.isValid())
        self.assertEqual(len(signalspy), 2)  # two calls of setCurrentIndex
         
        self.assertEqual(self.ui.fontComboBox.receivers(self.ui.fontComboBox.currentIndexChanged), 1)
         
        self.assertEqual(self.ui.fontComboBox.currentText(), self.ui.bloodTextEdit.fontFamily())
        self.assertEqual(self.ui.fontComboBox.currentText(), self.ui.renalTextEdit.fontFamily())
        self.assertEqual(self.ui.fontComboBox.currentText(), self.ui.liverTextEdit.fontFamily())
        self.assertEqual(self.ui.fontComboBox.currentText(), self.ui.thyroidTextEdit.fontFamily())
        self.assertEqual(self.ui.fontComboBox.currentText(), self.ui.electrolyteTextEdit.fontFamily())
        self.assertEqual(self.ui.fontComboBox.currentText(), self.ui.lipidTextEdit.fontFamily())
         
        # we iterate through signals (here were two)
        # signal[0] is the first given argument (of type int) - index of chosen font family
        for signal in signalspy:
            print("That was argument's value during setCurrentIndex (for font family change) execution: ", signal[0], "\n")
            print("So the font family changed to ", self.ui.fontComboBox.itemText(signal[0]), "\n")
 
 
    def test_closeBtnNotDisabled(self):
        self.assertTrue(self.ui.returnBtn.isEnabled())
         
    def test_printBtnNotDisabled(self):
        self.assertTrue(self.ui.printBtn.isEnabled())

